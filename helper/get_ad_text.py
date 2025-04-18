from openai import AzureOpenAI
from dotenv import load_dotenv
import os
import json
import re

load_dotenv()

# Initialize the client
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2023-05-15",
    azure_endpoint=os.getenv("LLM_ENDPOINT")
)



def get_ad_text(url_text: str):
    prompt = f'''
    Extract key product details from the given URL text and generate a short advertisement text (max 20 words).
    
    URL Text: "{url_text}"
    
    Respond in JSON format: {{"ad_text": "your generated ad text"}}
    '''
    
    response = client.chat.completions.create(
        model=os.getenv("DEPLOYMENT_NAME"),
        messages=[
            {"role": "system", "content": "You are an AI that generates short and engaging ad texts."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=50
    )
    
    result_text = response.choices[0].message.content
    return json.loads(result_text)["ad_text"]
if __name__ == "__main__":
    url_text = "Create a vibrant image of a sleek red car parked on a scenic overlook with the sunset in the background, emphasizing the car's glossy finish and modern design"
    response = get_ad_text(url_text)
    print(response)
