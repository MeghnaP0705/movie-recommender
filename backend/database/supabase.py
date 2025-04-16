from supabase import create_client, Client
import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

# Initialize Supabase client
supabase: Client = create_client(url, key)

# Store user embedding
def store_user_embedding(user_id, embedding):
    supabase.table("user_embeddings").insert({
        "user_id": user_id,
        "embedding": embedding
    }).execute()

# Fetch embeddings for a given user
def fetch_user_embeddings(user_id):
    result = supabase.table("user_embeddings").select("*").eq("user_id", user_id).execute()
    return result.data
