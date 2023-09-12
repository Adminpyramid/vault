import logging

import requests


class SecretManager:

    def __init__(self, token, base_url):
        self.token = token
        self.base_url = base_url
        logging.basicConfig(filemode='a', filename='../logs/pyshop.log', format='%(asctime)s - %(message)s',
                            level=logging.INFO)

        self.headers = {
            "X-Vault-Token": self.token,
            "accept": "*/*"
        }

    def delete_cubbyhole_folder(self, folder_name):
        url = f"{self.base_url}/v1/cubbyhole/{folder_name}"

        response = requests.delete(url, headers=self.headers)
        if response.status_code in [200, 204]:
            logging.info("The cubbyhole folder erased")
            return True
        else:
            logging.error("The error occur the cubbyhole folder not erased")
            return False

    def add_data_to_cubbyhole(self, path, data_dict):
        url = f"{self.base_url}/v1/cubbyhole/{path}"
        self.headers += {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = "&".join([f"{key}={value}" for key, value in data_dict.items()])
        response = requests.post(url, data=data, headers=self.headers)

        if response.status_code in [200, 204]:
            logging.info("new data added ****")
            return True
        else:
            logging.error("error occur no data added")
            return False

    def delete_user_from_cubbyhole(self, path, key):
        url = f"{self.base_url}/v1/cubbyhole/{path}"

        # Get the existing secret data
        response = requests.get(url, headers=self.headers)

        secret_data = response.json().get("data", {})

        if key in secret_data:
            # Delete the specified key
            del secret_data[key]

            # Update the secret data without the deleted key
            update_response = requests.post(url, json=secret_data, headers=self.headers)
            if update_response.status_code in [200, 204]:
                logging.info("user deleted")
                return True
            else:
                logging.error("Error occur no user deleted")
                return False
        return None

    def get_total_database_connections(self):
        url = f"{self.base_url}/v1/database/config?list=true"
        response = requests.get(url, headers=self.headers)
        if response.status_code in [200, 204]:
            logging.info("connections retrieved")
            return response
        else:
            logging.error("Error occur no retrieved connections")
            return False

    def get_database_details(self, database_name):
        url = f"{self.base_url}/v1/database/config/{database_name}"
        response = requests.get(url, headers=self.headers)
        if response.status_code in [200, 204]:
            logging.info("The database details retrieved")
            return response
        else:
            logging.info("Error occur failed to retrieve database details")
            return False

    def delete_database_configuration(self, database_name):
        url = f"{self.base_url}/v1/database/config/{database_name}"
        response = requests.delete(url, headers=self.headers)
        if response.status_code in [200, 204]:
            logging.info("The database conf deleted successfully")
            return True
        else:
            logging.error("Error failed to delete database configuration")
            return False

    def get_dynamic_role_credentials(self, role_name):
        url = f"{self.base_url}/v1/database/creds/{role_name}"
        response = requests.get(url, headers=self.headers)
        if response.status_code in [200, 204]:
            logging.info("The credential retrieved")
            response_data = response.json()
            return response_data["data"]
        else:
            logging.error("Error failed to retrieve credentials")
            return False

    def reset_database_plugin(self, database_connection):
        url = f"{self.base_url}/v1/database/reset/{database_connection}"
        response = requests.post(url, headers=self.headers)
        if response.status_code in [200, 204]:
            logging.info("Reset plugin success")
            return True
        else:
            logging.error("Error occur plugin not reset")
            return False

    def get_roles_of_login_user(self):
        url = f"{self.base_url}/v1/database/roles?list=true"
        response = requests.get(url, headers=self.headers)
        if response.status_code in [200, 204]:
            logging.info("The roles retrieved")
            return response
        else:
            logging.error("Error occur no role retrieved")
            return False

    def get_role_details(self, role_name):
        url = f"{self.base_url}/v1/database/roles/{role_name}"
        response = requests.get(url, headers=self.headers)
        if response.status_code in [200, 204]:
            logging.info("The role retrieved")
            return response
        else:
            logging.error("Error occur not role retrieved")
            return False

    def update_role(self, role_name, role_data):
        url = f"{self.base_url}/v1/database/roles/{role_name}"
        self.headers += {
            "Content-Type": "application/json"
        }
        response = requests.post(url, json=role_data, headers=self.headers)
        if response.status_code in [200, 204]:
            logging.info("Role updated")
            return True
        else:
            logging.error("Update failed")
            return False

    def delete_role(self, role_name):
        url = f"{self.base_url}/v1/database/roles/{role_name}"
        response = requests.delete(url, headers=self.headers)
        if response.status_code in [200, 204]:
            logging.info("operation success")
            return True
        else:
            logging.error("Operation failed")
            return False

    def rotate_role(self, role_name):
        url = f"{self.base_url}/v1/database/rotate-role/{role_name}"
        response = requests.post(url, headers=self.headers)
        if response.status_code in [200, 204]:
            logging.info("Operation pass")
            return True
        else:
            logging.error("Operation failed")
            return False

    def rotate_root(self, database_connection):
        url = f"{self.base_url}/v1/database/rotate-root/{database_connection}"
        response = requests.post(url, headers=self.headers)
        if response.status_code in [200, 204]:
            logging.info("The rotation success")
            return True
        else:
            logging.error("Rotation failed")
            return False

    def request_db_credentials(self, static_role):
        url = f"{self.base_url}/v1/database/static-creds/{static_role}"
        response = requests.get(url, headers=self.headers)
        if response.status_code in [200, 204]:
            logging.info("The request confirmed")
            return True
        else:
            logging.error("The request failed")
            return False

    def get_all_static_roles(self):
        url = f"{self.base_url}/v1/database/static-roles?list=true"
        response = requests.get(url, headers=self.headers)
        if response.status_code in [200, 204]:
            logging.info("The role retrieved")
            return response
        else:
            logging.error("Error occur")
            return False

    def manage_static_role(self, static_role):
        url = f"{self.base_url}/v1/database/static-roles/{static_role}"
        response = requests.get(url, headers=self.headers)
        if response.status_code in [200, 204]:
            logging.info("The activity success")
            return True
        else:
            logging.error("The activity failed")
            return False

    def delete_static_role(self, role_name):
        url = f"{self.base_url}/v1/database/static-roles/{role_name}"
        response = requests.delete(url, headers=self.headers)
        if response.status_code in [200, 204]:
            logging.info("The deletion complete")
            return True
        else:
            logging.error("Error occur")
            return False

    # by default, it accepts ttl inform of hour as parameter of input integer
    def create_vault_dynamic_role(self, connection_name, role_name, default_ttl, max_ttl):
        # Set the URL for the Vault API
        url = f"{self.base_url}/v1/database/roles/{role_name}"  # Use role_name parameter

        # Define the data payload
        data = {
            "db_name": connection_name,
            "creation_statements": [
                "CREATE ROLE \"{{name}}\" WITH LOGIN PASSWORD '{{password}}' VALID UNTIL '{{expiration}}';",
                "GRANT SELECT ON ALL TABLES IN SCHEMA public TO \"{{name}}\";",
                "GRANT CONNECT ON DATABASE pyshop TO \"{{name}}\";",
                # That  is the important statement for connection of the database to the server
                "ALTER USER \"{{name}}\" WITH SUPERUSER;"
            ],
            "revocation_statements": [
                "REVOKE ALL PRIVILEGES ON ALL TABLES IN SCHEMA public FROM \"{{name}}\";"
            ],
            "rollback_statements": [
                "DROP ROLE IF EXISTS \"{{name}}\";"
            ],
            "default_ttl": f"{default_ttl}h",  # Convert back to string with 'h'
            "max_ttl": f"{max_ttl}h"  # Convert back to string with 'h'
        }

        # Make the API request
        response = requests.post(url, headers=self.headers, json=data)

        # Check the response
        if response.status_code in [200, 204]:
            logging.info(f"Role created successfully!")
            return True
        else:
            logging.error(f"Error occur")
            return False

    def create_static_role(self, role_name, rotation_time, db_name, db_username):

        url = f"{self.base_url}/v1/database/static-roles/{role_name}"
        data = {
            "credential_config": {},
            "credential_type": "password",
            "db_name": {db_name},
            "rotation_period": {rotation_time},
            "rotation_statements": [
                "ALTER ROLE \"{{name}}\" WITH PASSWORD '\''{{password}}'\''",
                "SELECT now()"
            ],
            "username": {db_username}

        }

        response = requests.post(url, data=data, headers=self.headers)

        if response.status_code in [200, 204]:
            logging.info("Static role created successfully")
            return True
        else:
            logging.error(f"Error creating static role")
            return False

    def add_allowed_role_to_database_configuration(self, db_name, role_name):
        # Set the URL for the Vault API
        url = f"{self.base_url}/v1/database/config/{db_name}"
        # Define the data payload for updating the database configuration
        data = {
            "allowed_roles": role_name,  # Add the role to the allowed_roles list
        }

        # Make the API request to update the database configuration
        response = requests.post(url, headers=self.headers, json=data)

        # Check the response
        if response.status_code in [204, 200]:
            logging.info(f"Role added to the allowed roles for database successfully!")
            return True
        else:
            logging.error(f"Error")
            return False
