import base64
import logging
import time

import requests


class VaultTransitEncryption:

    def __init__(self, vault_address, vault_token):
        self.vault_address = vault_address
        self.vault_token = vault_token
        logging.basicConfig(filemode='a', filename='../logs/pyshop.log', format='%(asctime)s - %(message)s',
                            level=logging.INFO)

    def create_base_key(self, key_name):
        api_url = f"{self.vault_address}/v1/transit/keys/{key_name}"
        headers = {
            "X-Vault-Token": self.vault_token,
        }
        data = {
            "type": "aes256-gcm96",
        }
        response = requests.post(api_url, json=data, headers=headers)
        if response.status_code == 200:
            logging.info("New base key created")
            return True
        else:
            logging.error(response.json(), exc_info=True)
            return False

    def derive_data_key(self, base_key_name, context_string):
        api_url = f"{self.vault_address}/v1/transit/datakey/plaintext/{base_key_name}"
        context = base64.b64encode(context_string.encode()).decode()

        headers = {
            "X-Vault-Token": self.vault_token,
        }

        data = {
            "context": context,
            "derived": True
        }

        response = requests.post(api_url, json=data, headers=headers)
        if response.status_code == 200:
            result = response.json()
            logging.info("new derived key created *************************")
            return result.get("data", {}).get("ciphertext", "")
        else:
            logging.error(response.json(), exc_info=True)
            return False

    def encrypt_with_key(self, key_name, data_to_encrypt="default data", derive_cipher_text=""):

        api_url = f"{self.vault_address}/v1/transit/encrypt/{key_name}"
        logging.info("data encrypting ....")
        time.sleep(0.2)
        context = base64.b64encode(data_to_encrypt.encode()).decode()
        logging.info("******data base64 encoded successfully *****")

        headers = {
            "X-Vault-Token": self.vault_token,
        }
        data = {
            "plaintext": context,
            "cipher": derive_cipher_text
        }
        response = requests.post(api_url, json=data, headers=headers)
        if response.status_code == 200:
            result = response.json()
            logging.info("The data encrypted successfully")
            return result.get("data", {}).get("ciphertext", "")
        else:
            logging.error("The encryption process failed ", exc_info=True)
            return False

    def decrypt_with_key(self, key_name, ciphertext, derive_cipher_text=None):
        api_url = f"{self.vault_address}/v1/transit/decrypt/{key_name}"
        headers = {
            "X-Vault-Token": self.vault_token,
        }
        data = {
            "ciphertext": ciphertext,
            "cipher": derive_cipher_text
        }
        response = requests.post(api_url, json=data, headers=headers)
        if response.status_code == 200:
            result = response.json()
            output = result.get("data", {}.get("ciphertext", ""))["plaintext"]
            logging.info("The data decrypted  successfully ")
            return base64.b64decode(output.encode()).decode()
        else:
            logging.error("Failed to decryption the data", exc_info=True)
