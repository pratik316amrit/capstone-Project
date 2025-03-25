from openai import AzureOpenAI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import json

load_dotenv()

# Initialize the client
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2023-05-15",
    azure_endpoint=os.getenv("LLM_ENDPOINT")
)

class ProductCheck(BaseModel):
    is_product: bool  # True if the string describes a buyable product
    reason: str  # Explanation for the classification

def check_product(text: str):
    prompt = f'''
    Determine whether the given text is about a buyable product.
    
    Text: "{text}"
    
    Respond in JSON format: {{"is_product": true/false, "reason": "your explanation"}}
    '''
    
    response = client.chat.completions.create(
        model=os.getenv("DEPLOYMENT_NAME"),  # Ensure this matches your Azure OpenAI deployment
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
        max_tokens=200
    )
    
    result_text = response.choices[0].message.content
    return result_text

if __name__ == "__main__":
    text = "This new wireless headphone has noise cancellation and costs $99."
    response = check_product(text)
    print(response)
