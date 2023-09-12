# import requests
#
# # Set the URL for the Vault API
# url = "http://127.0.0.1:8200/v1/database/roles/my-role"  # Replace 'my-role' with your desired role name
#
# # Set the Vault token
# headers = {
#     "X-Vault-Token": "admin",  # Replace 'admin' with your actual Vault token
# }
#
# # Define the data payload
# data = {
#     "db_name": "vault",  # Replace 'vault' with your actual database name
#     "creation_statements": "CREATE ROLE \"{{name}}\" WITH LOGIN PASSWORD '{{password}}' VALID UNTIL '{{expiration}}';",
#     "revocation_statements": "REVOKE ALL PRIVILEGES ON ALL TABLES IN SCHEMA public FROM \"{{name}}\";",
#     "rollback_statements": "DROP ROLE IF EXISTS \"{{name}}\";"
# }
#
# # Make the API request
# response = requests.post(url, headers=headers, json=data)
#
# # Check the response
# if response.status_code == 200:
#     print("Role created successfully!")
# else:
#     print(f"Error: {response.status_code} - {response.text}")
# import os

# In your admin.py file

import os

import django

# Set the DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Pyshop.settings')

# Initialize Django
django.setup()

# Now you can access the cache
from django.core.cache import cache

# Clear the cache
cache.clear()
