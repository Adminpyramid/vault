import logging

import requests


class VaultUserManagement:
    def __init__(self, api_token, base_url):
        self.api_token = api_token
        self.base_url = base_url

    def enable_auth_method(self, auth_method):
        url = f"{self.base_url}/v1/sys/auth/{auth_method}"
        headers = {"X-Vault-Token": self.api_token}
        data = {"type": auth_method}
        if requests.post(url, headers=headers, json=data).status_code in [200, 204]:
            logging.info("Operation pass")
            return True
        else:
            logging.error("operation failed")
            return False

    def post_user_policies(self, username, token_policies):
        url = f"{self.base_url}/v1/auth/userpass/users/{username}/policies"
        headers = {
            "X-Vault-Token": self.api_token,
            "Content-Type": "application/json",
            "accept": "*/*"
        }
        data = {
            "token_policies": token_policies
        }
        if requests.post(url, json=data, headers=headers).status_code in [200, 204]:
            logging.info("Operation pass")
            return True
        else:
            logging.error("operation failed")
            return False

    def update_user_password(self, username, new_password):
        url = f"{self.base_url}/v1/auth/userpass/users/{username}/password"
        headers = {
            "X-Vault-Token": self.api_token,
            "Content-Type": "application/json",
            "accept": "*/*"
        }
        data = {
            "password": new_password
        }
        if requests.post(url, json=data, headers=headers).status_code in [200, 204]:
            logging.info("Operation pass")
            return True
        else:
            logging.error("operation failed")
            return False

    def delete_user(self, username):
        url = f"{self.base_url}/v1/auth/userpass/users/{username}"
        headers = {
            "X-Vault-Token": self.api_token,
            "accept": "*/*"
        }
        if requests.delete(url, headers=headers).status_code in [200, 204]:
            logging.info("Operation pass")
            return True
        else:
            logging.error("operation failed")
            return False

    def add_new_user(self, username, user_data):
        url = f"{self.base_url}/v1/auth/userpass/users/{username}"
        headers = {
            "X-Vault-Token": self.api_token,
            "Content-Type": "application/json",
            "accept": "*/*"
        }
        if requests.post(url, json=user_data, headers=headers).status_code in [200, 204]:
            logging.info("Operation pass")
            return True
        else:
            logging.error("operation failed")
            return False

    def get_user_details(self, username):
        url = f"{self.base_url}/v1/auth/userpass/users/{username}"
        headers = {
            "X-Vault-Token": self.api_token,
            "accept": "*/*"
        }
        return requests.get(url, headers=headers)

    def get_all_users(self):
        url = f"{self.base_url}/v1/auth/userpass/users?list=true"
        headers = {
            "X-Vault-Token": self.api_token,
            "accept": "*/*"
        }
        return requests.get(url, headers=headers)

    def login_with_userpass(self, username, password):
        url = f"{self.base_url}/v1/auth/userpass/login/{username}"
        headers = {
            "Content-Type": "application/json",
            "accept": "*/*"
        }
        data = {
            "password": password
        }
        response = requests.post(url, json=data, headers=headers)
        response_data = response.json()
        if response.status_code in [200, 204]:
            logging.info("Operation pass")
            return response_data.get('auth', {}).get('client_token')
        else:
            logging.error("operation failed")
            return False

    def github_user_mapping(self, query):
        url = f"{self.base_url}/v1/auth/github/map/users?list={query}"
        headers = {
            "X-Vault-Token": self.api_token,
            "accept": "*/*"
        }
        return requests.get(url, headers=headers)

    def github_map_users_with_key(self, key):
        url = f"{self.base_url}/v1/auth/github/map/users/{key}"
        headers = {
            "X-Vault-Token": self.api_token,
            "accept": "*/*"
        }
        return requests.get(url, headers=headers)

    def github_map_user_with_key(self, key, value):
        url = f"{self.base_url}/v1/auth/github/map/users/{key}"
        headers = {
            "X-Vault-Token": self.api_token,
            "Content-Type": "application/json",
            "accept": "*/*"
        }
        data = {
            "value": value
        }
        return requests.post(url, json=data, headers=headers)

    def github_delete_map_users_with_key(self, key):
        url = f"{self.base_url}/v1/auth/github/map/users/{key}"
        headers = {
            "X-Vault-Token": self.api_token,
            "accept": "*/*"
        }
        if requests.delete(url, headers=headers).status_code in [200, 204]:
            logging.info("Operation pass")
            return True
        else:
            logging.error("Operation failed")
            return False

    def login_with_token(self, token):
        url = f"{self.base_url}/v1/auth/token/lookup"
        headers = {
            "X-Vault-Token": self.api_token,
            "accept": "*/*"
        }
        if requests.post(url, headers=headers).status_code in [200, 204]:
            logging.info("Operation success")
            return True
        else:
            logging.error("Operation failed")
            return False

    def login_with_github(self, token):
        url = f"{self.base_url}/v1/auth/github/login"
        headers = {
            "X-Vault-Token": self.api_token,
            "Content-Type": "application/json",
            "accept": "*/*"
        }
        data = {
            "token": token
        }
        if requests.post(url, json=data, headers=headers).status_code in [200, 204]:
            logging.info("Operation pass")
            return True
        else:
            logging.error("Operation failed")
            return False


supported_auth_methods = [
    "token",
    "userpass",
    "ldap",
    "approle",
    "github",
    "gitlab",
    "aws",
    "azure",
    "kubernetes",
    "okta",
    "radius",
    "jwt",
    "oidc",
    "cert"
]
