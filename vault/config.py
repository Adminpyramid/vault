# Author Admin
# date  7 Septemba 2023 10:31:45 asubuhi EAT
# procedure The file must first run before any operation

from SecretManager import SecretManager

# Example usage with multiple key-value pairs
data_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}

data_static_role = {
    "db_name": "pyshop",
    "username": "postgres",
    "password": "7719",
    "creation_statements": ["ALTER ROLE \"{{name}}\" WITH PASSWORD '{{password}}';"],
    # "ALTER ROLE \"{{name}}\" WITH PASSWORD '{{password}}';"
    "default_ttl": "10m",  # Set the desired TTL
    "max_ttl": "10m",  # Set the desired max TTL
}

data_static_role_i = {
    "db_name": "pyshop",
    "username": "postgres",
    "password": "7719",
    "creation_statements": ["ALTER ROLE \"{{name}}\" WITH PASSWORD '{{password}}';"],
    # "ALTER ROLE \"{{name}}\" WITH PASSWORD '{{password}}';",
    "revocation_statements": "REVOKE ALL PRIVILEGES ON ALL TABLES IN SCHEMA public FROM \"{{name}}\";",
    "rollback_statements": "DROP ROLE IF EXISTS \"{{name}}\";",

}

# Example usage:
role_name = "kassim"
connection_name = "vault"
creation_statements = "CREATE ROLE \"{{name}}\" WITH LOGIN PASSWORD '{{password}}' VALID UNTIL '{{expiration}}';"
revocation_statements = "REVOKE ALL PRIVILEGES ON ALL TABLES IN SCHEMA public FROM \"{{name}}\";"
rollback_statements = "DROP ROLE IF EXISTS \"{{name}}\";"

################## SecretManager.static role data

data = {
    'db_name': 'vault',
    'creation_statements': "CREATE ROLE \"{{name}}\" WITH LOGIN PASSWORD '{{password}}'",
    'default_ttl': '1h',
    'max_ttl': '1h',
    'username': 'postgres',  # Replace with the desired username
    'rotation_period': '1h'  # Add rotation_period
}

####################### Database manager


# # Create an instance of VaultDatabaseManager with your base URL and token
# vault_database_manager = VaultDatabaseManager(base_url="http://localhost:8200", token="admin")
#
# print(SecretManager("admin","http://127.0.0.1:8200").delete_static_role("pt_student"))
# print(SecretManager("admin","http://127.0.0.1:8200").create_vault_dynamic_role("vault", "my-role", 1, 1))


############################# RabbitMq

# Usage example:
# if __name__ == "__main__":
#     vault_api = VaultRabbitMQAPI("http://127.0.0.1:8200", "admin")

# response_text = vault_api.make_request("POST", "http://localhost:15672/api", json_data={"message": "hello"})
# print(response_text)
#
# # Establish a RabbitMQ connection
# connection_uri = "http://127.0.0.1:15672"
# username = "guest"
# password = "guest"
# connection_response = vault_api.establish_rabbitmq_connection(connection_uri, username, password)
# print("Establish RabbitMQ Connection Response:", connection_response)

# result = vault_api.list_rabbitmq_roles()
# print(result)
# a = vault_api.create_rabbitmq_role("pyramid")
# print(a)
#
# queue_name = 'Nyau'
# message = 'high definition technology eneryne.com'
#
# credential = vault_api.get_rabbitmq_creds("pyramid")
# # Publish a message to the specified queue
# a = vault_api.publish_message_to_queue(credential, queue_name, message)
# print(a)


#################### Rabbit payload

payload = {

    "tags": "tag1,tag2",
    "vhosts": "{\"/\":{\"configure\":\".*\",\"write\":\".*\",\"read\":\".*\"}}",
    "vhost_topics": "{\"/\":{\"amq.topic\":{\"write\":\".*\",\"read\":\".*\"}}}"

}

####################### UserManagement

# importants attribute

# Example user data with password
user_data = {
    "password": "abuja",
    "token_bound_cidrs": [" 127.0.0.0/24"],
    "token_explicit_max_ttl": "1h",
    "token_max_ttl": "1h",
    "token_no_default_policy": False,
    "token_num_uses": 100,
    "token_period": "1h",
    "token_policies": ["dynamic"],
    "token_ttl": "1h",
    "token_type": "default"
}

################################# Clear out Postgres database

# DROP SCHEMA public CASCADE;
# CREATE SCHEMA public;
# DROP DATABASE database_name;

# SELECT 'DROP ROLE IF EXISTS "' || rolname || '";' FROM pg_roles;
# Save the returned values into sql file like delete.sql
# psql -U your_superuser_username -d your_database_name -a -f drop_roles.sql

# print(VaultUserManagement("admin", "http://127.0.0.1:8200").enable_auth_method("userpass"))
# print(VaultUserManagement("admin", "http://127.0.0.1:8200").enable_auth_method("approle"))
# print(VaultAppRoleManager("http://127.0.0.1:8200","admin").create_approle("myrole", "admin", "", ""))
# id = VaultAppRoleManager("http://127.0.0.1:8200","admin").retrieve_role_id("myrole")
# password= VaultAppRoleManager("http://127.0.0.1:8200","admin").generate_secret_id("myrole")
# print(id, ">>>>>>>>>>>>>>>>>>>>>>", password)
# tttt = VaultAppRoleManager("http://127.0.0.1:8200", "").login_with_approle(id, password)
# os.environ["DB_TOKEN"] =tttt
# print(os.environ.get("DB_TOKEN"))
# print(SecretManager( tttt, "http://127.0.0.1:8200").get_total_database_connections().status_code)


# print(SearchEngineManager("admin", "http://127.0.0.1:8200").enable_secret_engine("database"))

# lists  =  ["staff", "pt_student", "intent", "my-role", "guava"]
# accepted_roles = list(lists)
# accepted_roles = json.dumps(accepted_roles)
# acceptable_roles = ["my-role", "admin", "staff", "student", "intent"]
# result = VaultDatabaseManager("http://127.0.0.1:8200", "admin").create_database_connection("vault",  "postgres","7719","127.0.0.1", acceptable_roles, "pyshop")
#
# print(result)

print(SecretManager("admin", "http://127.0.0.1:8200").create_vault_dynamic_role("vault", "staff", 1, 24))
# allowed =["admin", "pyramid", "staff", "jam", "pyshop2"]
# print(SecretManager("admin", "http://127.0.0.1:8200").add_allowed_role_to_database_configuration("vault",allowed))
# print(VaultUserManagement("admin", "http://127.0.0.1:8200").add_new_user("ester", user_data))
