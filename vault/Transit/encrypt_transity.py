import requests


def create_transit_base_key(vault_address, vault_token, key_name):
    api_url = f"{vault_address}/v1/transit/keys/{key_name}"
    headers = {
        "X-Vault-Token": vault_token,
    }
    data = {
        "type": "aes256-gcm96"
    }
    response = requests.post(api_url, json=data, headers=headers)
    return response.json()


def derive_data_key(vault_address, vault_token, base_key_name, context):
    api_url = f"{vault_address}/v1/transit/datakey/plaintext/{base_key_name}"
    headers = {
        "X-Vault-Token": vault_token,
    }
    data = {
        "context": context
    }
    response = requests.post(api_url, json=data, headers=headers)
    return response.json()


def encrypt_with_derived_key(vault_address, vault_token, base_key_name, data_key_ciphertext, data_to_encrypt):
    api_url = f"{vault_address}/v1/transit/encrypt/{base_key_name}"
    headers = {
        "X-Vault-Token": vault_token,
    }
    data = {
        "ciphertext": data_key_ciphertext,
        "plaintext": data_to_encrypt
    }
    response = requests.post(api_url, json=data, headers=headers)
    return response.json()


# Replace with your actual Vault address and token
vault_address = "http://localhost:8200"
vault_token = "admin"

# Replace with your desired key name and encryption context
base_key_name = "my-key"
encryption_context = "YWRtaW4="
data_to_encrypt = "YWRtaW4="

# Create base key
base_key_info = create_transit_base_key(vault_address, vault_token, base_key_name)

# Derive data key
data_key_ciphertext = derive_data_key(vault_address, vault_token, base_key_name, encryption_context)["data"][
    "ciphertext"]

# Encrypt data using derived key
encrypted_data = encrypt_with_derived_key(vault_address, vault_token, base_key_name, data_key_ciphertext,
                                          data_to_encrypt)

# Print the encrypted data
print(encrypted_data)
