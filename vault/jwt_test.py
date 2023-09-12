import datetime

import jwt

# Sample payload (claims)
payload = {
    "sub": "1234567890",  # Subject
    "name": "John Doe",
    "iat": datetime.datetime.utcnow(),
    "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
}

# Secret key for signing
secret_key = "your-secret-key"

# Create the JWT
token = jwt.encode(payload, secret_key, algorithm="HS256")
print("Generated JWT:", token)

print(jwt.decode(token, "your-secret-key", algorithms=["HS256"]))
