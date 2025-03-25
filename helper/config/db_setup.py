from azure.storage.blob import BlobServiceClient
from azure.core.exceptions import ResourceExistsError
import os
from dotenv import load_dotenv

load_dotenv()


# Replace these with your actual values
BLOB_CONNECTION_ENDPOINT = os.getenv("BLOB_CONNECTION_ENDPOINT")
CONTAINER_NAME = os.getenv("CONTAINER_NAME")


# Create a BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(BLOB_CONNECTION_ENDPOINT)

# Get a ContainerClient
container_client = blob_service_client.get_container_client(CONTAINER_NAME)

# Check if the container exists before creating
try:
    container_client.create_container()
    print(f"Container '{CONTAINER_NAME}' created successfully.")
except ResourceExistsError:
    print(f"Container '{CONTAINER_NAME}' already exists. Skipping creation.")

# Export container_client for other files to use
