from dotenv import load_dotenv
import os

# First load from .env file
load_dotenv(override=True)

# Get the value of an environment variable
print(os.getenv('GOOGLE_API_KEY'))

# After modifying the .env file, call load_dotenv() again to reload changes
load_dotenv(override=True)

# Get the updated value
print(os.getenv('GOOGLE_API_KEY'))
