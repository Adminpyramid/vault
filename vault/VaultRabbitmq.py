import json
import logging

import pika
import requests


class VaultRabbitMQAPI:
    def __init__(self, vault_url, vault_token):
        self.vault_url = vault_url.rstrip('/')  # Ensure no trailing slash
        self.vault_token = vault_token
        self.headers = {
            "Accept": "*/*",
            "X-Vault-Token": self.vault_token,
        }

        logging.basicConfig(filemode='a', filename='../logs/pyshop.log', format='%(asctime)s - %(message)s',
                            level=logging.INFO)

    def make_request(self, method, url, json_data=None):
        response = requests.request(method, url, headers=self.headers, json=json_data)
        if response.status_code in [200, 204]:
            logging.info("Operation success")
            return True
        else:
            logging.error("Operation failed")
            return False

    def enable_rabbitmq(self, plugin_name, backend_type="plugin"):
        url = f"{self.vault_url}/v1/sys/mounts/rabbitmq"
        data = {
            "type": backend_type,
            "plugin_name": plugin_name,
        }
        if self.make_request("POST", url, json_data=data) in [200, 204]:
            logging.info("Operation Success")
            return True
        else:
            logging.error("Operation failed")
            return False

    def disable_rabbitmq(self):
        url = f"{self.vault_url}/v1/sys/mounts/rabbitmq"
        if self.make_request("DELETE", url).status_code in [200, 204]:
            logging.info("Operation success")
            return True
        else:
            logging.error("Operation Failed")
            return False

    def establish_rabbitmq_connection(self, connection_uri, username, password):
        url = f"{self.vault_url}/v1/rabbitmq/config/connection"
        data = {
            "connection_uri": connection_uri,
            "username": username,
            "password": password,
            "verify_connection": True
        }
        result = self.make_request("POST", url, json_data=data)
        if result.status_code in [200, 204]:
            logging.info("The new connection established")
            return True
        else:
            logging.error("The error occured in establishing new connection", exc_info=True)
            return False

    def create_rabbitmq_role(self, role_name, payload):
        url = f"http://{self.vault_url}/v1/rabbitmq/roles/{role_name}"

        # Convert the payload to a JSON string
        payload_json = json.dumps(payload)

        # Make the POST request
        response = requests.post(url, headers=self.headers, data=payload_json)

        # Check the response
        if response.status_code in [200, 204]:
            logging.info("new role created %s", role_name)
            return True
        else:
            logging.error("failed to create new role", exc_info=True)
            return False

    def list_rabbitmq_roles(self):
        url = f"{self.vault_url}/v1/rabbitmq/roles?list=true"
        result = self.make_request("GET", url)

        if result.status_code in [200, 204]:
            logging.info("list retrieved successfully")
            return result.json()["data"]["keys"]
        else:
            logging.error("The error has occur ", exc_info=True)
            return False

    def delete_rabbitmq_role(self, role_name):
        url = f"{self.vault_url}/v1/rabbitmq/roles/{role_name}"
        result = self.make_request("DELETE", url)

        if result.status_code in [200, 204]:
            logging.info("The role erased %s", role_name)
            return True
        else:
            logging.error("The erased failed for role %s", role_name)
            return False

    def get_rabbitmq_creds(self, role_name):
        url = f"{self.vault_url}/v1/rabbitmq/creds/{role_name}"
        result = self.make_request("GET", url)

        if result.status_code in [200, 204]:
            logging.info("The credentials for role_name = %s retrieved", role_name)
            return result.json()["data"]
        else:
            logging.error("un able to retrieve the credentials for role %s ")
            return False

    def publish_message_to_queue(self, credential, queue_name, message):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host='127.0.0.1',
                port=5672,
                virtual_host='/',
                credentials=pika.PlainCredentials(
                    username=credential['username'],
                    password=credential['password']
                )
            )
        )

        channel = connection.channel()

        channel.queue_declare(queue=queue_name)

        channel.basic_publish(exchange='', routing_key=queue_name, body=message)

        connection.close()
