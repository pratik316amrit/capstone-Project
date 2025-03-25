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

def transform_query(url_text: str):
    prompt = f'''
    Extract relevant product details from the given text URL and generate an advertisement prompt for DALL·E.
    
    URL Text: "{url_text}"
    
    Respond in JSON format: {{"prompt": "your generated DALL·E advertisement prompt"}}
    '''
    
    response = client.chat.completions.create(
        model=os.getenv("DEPLOYMENT_NAME"),
        messages=[
            {"role": "system", "content": "You are an AI that generates advertisement prompts for DALL·E."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
        max_tokens=200
    )
    
    result_text = response.choices[0].message.content
    return result_text

if __name__ == "__main__":
    url_text = "https://www.google.com/search?q=a+red+car&oq=a+red+&gs_lcrp=EgRlZGdlKgkIABBFGDsY-QcyCQgAEEUYOxj5BzIHCAEQABiABDIGCAIQRRg5MgcIAxAAGIAEMgcIBBAAGIAEMgYIBRBFGDwyBggGEEUYPDIGCAcQRRg8MgYICBBFGEHSAQgzNjc5ajBqMagCALACAA&sourceid=chrome&ie=UTF-8"
    response = transform_query(url_text)
    print(response)