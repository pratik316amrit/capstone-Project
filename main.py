from flask import Flask, request, jsonify
from flask_cors import CORS
import uuid
from helper.config.db_setup import blob_service_client
import os
from dotenv import load_dotenv
from helper.transform_query import transform_query
from helper.get_ad_text import get_ad_text
import base64

load_dotenv()


from helper.check_product import check_product
from helper.download_blob import download_blob
from helper.upload_blob import upload_string
from helper.random_blob import get_random_blob
from helper.get_image import get_image
from helper.poster_text import poster_text

app = Flask(__name__)
CORS(app)  # Allow requests from your Chrome extension

def generate_unique_blob_name(base_name):
    """Generates a unique blob name using UUID."""
    return f"{base_name}_{uuid.uuid4().hex}"

@app.route('/api/track', methods=['POST'])
def track():
    try:
        data = request.get_json()  # Get JSON data from request
        if not data or 'url' not in data:
            return jsonify({"error": "Invalid data"}), 400

        url = data['url']
        print(f"Tracked URL: {url}")

        # Check if it is about an product or not

        is_product = check_product(url)
        print(f"Is product: {is_product}")

        if(is_product):
            blobname = generate_unique_blob_name(url)
            upload_string(blob_service_client, os.getenv("CONTAINER_NAME"), url, blobname)

            return jsonify({"message": "URL tracked successfully"}), 200
        else:
            return jsonify({"message": "URL is not in blob"}), 405

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route('/api/ad', methods=['GET'])
def get_ad():
    blob_name = get_random_blob()
    print(blob_name)
    if not blob_name:
        return jsonify({"error": "No ad available"}), 404
    
    blob_data = download_blob(blob_name)
    transformed_ad_query = transform_query(blob_data['text_content'])
    
    ad_text = get_ad_text(transformed_ad_query)
    tag_text = poster_text(transformed_ad_query)
    print(tag_text)
    print(transformed_ad_query)

    image = get_image(transformed_ad_query,tag_text)
    
    # Encode image in base64
    image_base64 = base64.b64encode(image).decode('utf-8')
    print(image_base64)
    
    return jsonify({
        "ad_text": ad_text,
        "image_base64": image_base64
    })



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
