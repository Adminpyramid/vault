import requests

base_url = "http://127.0.0.1:5000"  # Replace with your actual Flask app URL

# Make a GET request to the /get_cubby_data endpoint
response = requests.get(f"{base_url}/get_cubby_data")

if response.status_code == 200:
    data = response.json()
    print("Retrieved data:", data)
else:
    print("Error:", response.text)
