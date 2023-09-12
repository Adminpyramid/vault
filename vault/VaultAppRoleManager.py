import json
import logging

import requests


class VaultAppRoleManager:
    def __init__(self, vault_url, vault_token):
        self.vault_url = vault_url
        self.vault_token = vault_token
        self.headers = {
            "X-Vault-Token": self.vault_token
        }

    def auth_approle(self, role_id, secret_id):
        auth_data = {
            "role_id": role_id,
            "secret_id": secret_id
        }
        response = requests.post(f"{self.vault_url}/v1/auth/approle/login", data=json.dumps(auth_data),
                                 headers=self.headers)
        if response.status_code in [200, 204]:
            logging.info("Operation pass")
            return response.json()
        else:
            logging.error("Operation failed")
            return False

    def deauth_approle(self, token):
        response = requests.post(f"{self.vault_url}/v1/auth/token/revoke-self", headers=self.headers)
        if response.status_code in [204, 200]:
            logging.info("Operation pass")
            return True
        else:
            logging.error("Operation failed")
            return False

    def create_approle(self, role_name, policies, token_ttl, token_max_ttl):
        data = {
            "policies": policies,
            "token_ttl": token_ttl,  # Set the token's TTL (default: 1 hour)
            "token_max_ttl": token_max_ttl  # Set the token's maximum TTL (default: 24 hours)
        }
        response = requests.post(f"{self.vault_url}/v1/auth/approle/role/{role_name}", data=json.dumps(data),
                                 headers=self.headers)
        if response.status_code in [204, 200]:
            logging.info("Operation pass")
            return True
        else:
            logging.error("Operation failed")
            return False

    def retrieve_role_id(self, role_name):
        response = requests.get(f"{self.vault_url}/v1/auth/approle/role/{role_name}/role-id", headers=self.headers)
        if response.status_code in [200, 204]:
            return response.json().get("data", {}).get("role_id")
        else:
            return False

    def delete_approle(self, role_name):
        response = requests.delete(f"{self.vault_url}/v1/auth/approle/role/{role_name}", headers=self.headers)
        if response.status_code in [204, 200]:
            logging.info("Operation pass")
            return True
        else:
            logging.error("Operation failed")
            return False

    def generate_secret_id(self, role_name):
        response = requests.post(f"{self.vault_url}/v1/auth/approle/role/{role_name}/secret-id", headers=self.headers)
        if response.status_code in [200, 204]:
            logging.info("Operation success")
            return response.json().get("data", {}).get("secret_id")
        else:
            logging.error("Operation failed")
            return False

    def login_with_approle(self, role_id, secret_id):
        auth_response = self.auth_approle(role_id, secret_id)
        if auth_response and "auth" in auth_response:
            return auth_response["auth"]['client_token']
        else:
            return None
