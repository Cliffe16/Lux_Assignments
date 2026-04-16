import requests
from config import NEWS_API_KEY


def extract_news():
    # Define url and parameters
    url = "https://newsapi.org/v2/everything"
    params = {
        'q': 'Iran',
        'apiKey': {'API_KEY'},
        'from': '2026-04-15',
        'sortBy': 'popularity'
    }
    
    try:
        # Send request to url
        response = requests.get(url, params=params)
        # Raise error if request failes
        response.raise_for_status()

        # Store response in json
        data = response.json()

        # Retreive the articles item as a list from the nested json returned
        articles = data.get("articles", [])

        return articles

    except requests.exceptions.RequestException as e:
        print("Error fetching data: ", e)
