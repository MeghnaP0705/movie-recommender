import openai
import os
from dotenv import load_dotenv
load_dotenv()  
openai.api_key = os.getenv("GEMINI_API_KEY")

def get_embedding(text):
    response = openai.Embedding.create(input=[text], model="textembedding-gecko-001")
    return response['data'][0]['embedding']
