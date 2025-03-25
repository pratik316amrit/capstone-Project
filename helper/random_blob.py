# main.py
import random
from helper.config.db_setup import container_client

def get_random_blob():
    """
    Fetch a random blob name from the Azure container.
    """
    try:
        # List all blobs in the container
        blobs = list(container_client.list_blobs())

        if not blobs:
            print("No blobs found in the container.")
            return None

        # Select a random blob
        random_blob = random.choice(blobs)
        print(f"Randomly selected blob: {random_blob.name}")
        
        return random_blob.name
    except Exception as e:
        print(f"Error fetching random blob: {str(e)}")
        return None

# Example Usage
if __name__ == "__main__":
    random_blob_name = get_random_blob()
