# Author Admin
# date 28 Agosti 2023 03:53:45 alasiri EAT
# procedure Describes the clear steps of create a connection to database

"""  That is pre-requirements for postgresql
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO username;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO username;
GRANT ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public TO username;

to solve this use postgres user
"""
import logging

import requests


class VaultDatabaseManager:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token

        self.headers = {
            "X-Vault-Token": self.token,
            "Content-Type": "application/json",
            "accept": "application/json",
        }

    def create_database_connection(self, connection_name, db_username, db_password, db_ip, accepted_roles_list, DB):
        url = f"{self.base_url}/v1/database/config/{connection_name}"
        connection_data = {
            "plugin_name": "postgresql-database-plugin",
            "allowed_roles": accepted_roles_list,
            "connection_url": r"postgresql://{{username}}:{{password}}" + f"@{db_ip}:5432/{DB}",
            "username": db_username,
            "password": db_password,
            "verify_connection": True,
        }
        # print(connection_data) # Normal used for debug purpose
        response = requests.post(url, json=connection_data, headers=self.headers)
        if response.status_code in [200, 204]:
            logging.info("Operation pass")
            return True
        else:
            logging.error("Operation Failed %s", response.json())
            return False

    def delete_database_connection(self, connection_name):
        url = f"{self.base_url}/v1/database/config/{connection_name}"
        response = requests.delete(url, headers=self.headers)
        if response.status_code in [200, 204]:
            logging.info("Operation success")
            return True
        else:
            logging.error("operation failed")
            return False

    def update_database_connection(self, connection_name, updated_connection_data):
        url = f"{self.base_url}/v1/database/config/{connection_name}"
        response = requests.put(url, json=updated_connection_data, headers=self.headers)
        if response.status_code in [200, 204]:
            logging.info("Operation pass")
            return True
        else:
            logging.info("Operation Failed")
            return False
