import httpx
from typing import List, Dict

JOKE_API_URL = "https://sv443.net/jokeapi/v2/joke/Any?lang=en&amount=100"

def fetch_jokes() -> List[Dict]:
    """
    Fetches jokes from the JokeAPI.
    """
    try:
        response = httpx.get(JOKE_API_URL)
        response.raise_for_status()
        jokes = response.json()["jokes"]
        processed_jokes = []

        for joke in jokes:
            if joke["type"] == "single":
                processed_jokes.append({
                    "category": joke["category"],
                    "type": joke["type"],
                    "joke": joke["joke"],
                    "setup": None,
                    "delivery": None,
                    "nsfw": joke["flags"]["nsfw"],
                    "political": joke["flags"]["political"],
                    "sexist": joke["flags"]["sexist"],
                    "safe": joke["safe"],
                    "lang": joke["lang"]
                })
            elif joke["type"] == "twopart":
                processed_jokes.append({
                    "category": joke["category"],
                    "type": joke["type"],
                    "joke": None,
                    "setup": joke["setup"],
                    "delivery": joke["delivery"],
                    "nsfw": joke["flags"]["nsfw"],
                    "political": joke["flags"]["political"],
                    "sexist": joke["flags"]["sexist"],
                    "safe": joke["safe"],
                    "lang": joke["lang"]
                })

        return processed_jokes
    except httpx.RequestError as e:
        print(f"An error occurred while fetching jokes: {e}")
        return []
