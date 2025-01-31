import jwt
import time

# Your secret key and algorithm
secret_key = "your_jwt_secret_key"
algorithm = "HS256"

# Current time and expiration time (5 minutes from now)
current_time = int(time.time())  # Current UNIX timestamp
expiration_time = current_time + 60 * 60  # Add 5 minutes (5 * 60 seconds)

# Payload data
payload = {
    "user": 123,
    "username": "example_user",
    "exp": expiration_time  # Expiration time
}

# Create the token
token = jwt.encode(payload, key=secret_key, algorithm=algorithm)
print(f"Generated Token: {token}")

# Decode the token for verification
decoded_payload = jwt.decode(token, key=secret_key, algorithms=[algorithm])
print(f"Decoded Payload: {decoded_payload}")
