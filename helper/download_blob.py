
from helper.config.db_setup import container_client
from helper.random_blob import get_random_blob

def download_blob(blob_name):
    """
    Download the specified blob and extract its text content.
    """
    try:
        # Get blob client
        blob_client = container_client.get_blob_client(blob_name)

        # Download blob content
        blob_data = blob_client.download_blob().readall()

        # Convert bytes to string (assuming it's a text file)
        text_content = blob_data.decode('utf-8')
        
        print(f"Content of {blob_name}:\n{text_content}")

        return {"blob_name": blob_name, "text_content": text_content}
    except Exception as e:
        print(f"Error downloading blob '{blob_name}': {str(e)}")

# Example Usage
if __name__ == "__main__":
    blob_name = get_random_blob()
    if blob_name:
        result = download_blob(blob_name)
        print(result['text_content'])