import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api.api-ninjas.com/v1/animals"
API_KEY = os.getenv("API_KEY")


def fetch_data(animal_name):
    """Gets the animals from the API. Returns a list of dictionaries."""
    headers = {"X-Api-Key": API_KEY}
    params = {"name": animal_name}
    response = requests.get(API_URL, headers=headers, params=params)
    return response.json()