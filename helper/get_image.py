import base64
import os
import json
import requests
from flask import Flask, jsonify
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

client = AzureOpenAI(
    api_version="2024-02-01",
    azure_endpoint="",
    api_key=os.getenv("DALLE_OPENAI_API_KEY")  # Use environment variable for security
)

    
def get_image(prompt, poster_text):
    combined_prompt = f"{prompt} with a promotional banner saying: '{poster_text}'"
    result = client.images.generate(
        model="dall-e-3",  # the name of your DALL-E 3 deployment
        prompt=combined_prompt,
        n=1
    )
    image_url = json.loads(result.model_dump_json())["data"][0]["url"]
    
    # Download the image
    response = requests.get(image_url)
    
    if response.status_code == 200:
        image_data = response.content
        with open("generated_image.png", "wb") as file:
            file.write(image_data)  # Save the image to a file
        print("Image saved as generated_image.png")
        return image_data
    else:
        print("Failed to download image")
        return None


if __name__ == "__main__":
    prompt = "Create an image of a sleek red car parked on a scenic overlook with the sunset in the background, reflecting the car's shiny surface."

    poster_text = "Sleek. Glossy. Modern."

    image = get_image(prompt,poster_text)
    print(image)
    