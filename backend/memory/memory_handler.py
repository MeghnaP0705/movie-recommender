from database.supabase import store_user_embedding, fetch_user_embeddings
from utils.embeddings import get_embedding

def remember_preference(user_id, preference_text):
    embedding = get_embedding(preference_text)
    store_user_embedding(user_id, embedding)

def get_preferences(user_id):
    return fetch_user_embeddings(user_id)
