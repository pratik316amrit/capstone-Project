import logging
from azure.storage.blob import BlobServiceClient

# Configure logging
logging.basicConfig(level=logging.INFO)

def upload_string(blob_service_client, container_name, content, blob_name):
    """
    Uploads a string as a blob to Azure Blob Storage.

    :param blob_service_client: Instance of BlobServiceClient
    :param container_name: Name of the Azure storage container
    :param content: The string content to upload
    :param blob_name: Destination blob name in the container
    """
    try:
        # Get the blob client
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

        # Upload the string as a blob
        blob_client.upload_blob(content, overwrite=True)

        logging.info(f"Uploaded string content to Azure Blob Storage as {blob_name}")
    except Exception as e:
        logging.error(f"Failed to upload string content: {str(e)}")

# Example Usage
if __name__ == "__main__":
    CONNECTION_STRING = ""
    CONTAINER_NAME = ""

    # Initialize BlobServiceClient
    blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)

    content = "This is a sample text content."
    blob_name = "sampletext.txt"

    upload_string(blob_service_client, CONTAINER_NAME, content, blob_name)
