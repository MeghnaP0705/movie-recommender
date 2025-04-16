from tools.tmdb_tool import get_movie_info
from tools.user_profile_tool import summarize_preferences
from memory.memory_handler import remember_preference, get_preferences

def movie_agent(user_id, query):
    query = query.lower()

    if "like" in query or "preference" in query:
        remember_preference(user_id, query)
        return "Got it! I'll remember that."

    if "recommend" in query or "suggest" in query:
        prefs = get_preferences(user_id)
        summary = summarize_preferences(prefs)

        genre = None
        for word in summary.split():
            if word.lower() in ["sci-fi", "comedy", "drama", "thriller", "horror", "romance"]:
                genre = word
                break

        if not genre:
            return "Sorry, I couldn't detect your genre preference."

        movies = get_movie_info(genre)
        if not movies.get("results"):
            return "I couldn't find any movie matching your preferences."

        movie_title = movies["results"][0]["title"]
        return f"Based on your preference: {summary}, try: {movie_title}"

    return "Can you rephrase your request?"
