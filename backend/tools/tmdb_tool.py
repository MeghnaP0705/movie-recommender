import requests, os
from dotenv import load_dotenv
load_dotenv()  
def get_movie_info(genre_name, language='en'):
    api_key = os.getenv("TMDB_API_KEY")

    # Map genre names to IDs (you could cache or fetch this dynamically)
    genre_map = {
        "sci-fi": 878,
        "science fiction": 878,
        "comedy": 35,
        "drama": 18,
        "thriller": 53,
        "horror": 27,
        "romance": 10749,
        "crime": 80
    }

    genre_id = genre_map.get(genre_name.lower())
    if not genre_id:
        return {}

    url = (
        f"https://api.themoviedb.org/3/discover/movie"
        f"?api_key={api_key}&with_genres={genre_id}&language={language}"
        f"&sort_by=popularity.desc"
    )
    response = requests.get(url)
    return response.json()

