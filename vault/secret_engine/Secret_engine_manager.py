import logging

import requests


class SearchEngineManager:
    def __init__(self, token, vault_address):
        self.token = token
        self.vault_address = vault_address
        logging.basicConfig(filemode='a', filename='../logs/pyshop.log', format='%(asctime)s - %(message)s',
                            level=logging.INFO)

    def list_supported_secret_engines(self):
        supported_engines = ["kv", "database", "google", "aws", "transit", "ssh"]  # Add more as needed
        logging.info("List of supported secret engine retrieved")
        return supported_engines

    def enable_secret_engine(self, engine_name):
        url = f"{self.vault_address}/v1/sys/mounts/{engine_name}"
        headers = {"X-Vault-Token": self.token}
        data = {"type": engine_name}  # Replace with the appropriate engine type

        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 204:
            logging.info("NEW secret engine enebled")
            return True
        else:
            logging.error(response.json(), exc_info=True)
            return False

    def disable_secret_engine(self, engine_name):
        url = f"{self.vault_address}/v1/sys/mounts/{engine_name}"
        headers = {"X-Vault-Token": self.token}

        response = requests.delete(url, headers=headers)

        if response.status_code == 204:
            logging.info("secret engine stopped")
            return True
        else:
            logging.error("Failed to kill secret engine", exc_info=True)
            return False

    def list_enabled_engines(self):
        url = f"{self.vault_address}/v1/sys/mounts"
        headers = {"X-Vault-Token": self.token}

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            engines = response.json()
            enabled_engines = [engine for engine in engines.keys()]
            logging.info("The enabled secret engine retrieved ")
            return enabled_engines
        else:
            logging.error("  failed to list all enabled engines ", exc_info=True)
            return 0
