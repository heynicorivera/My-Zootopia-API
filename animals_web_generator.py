import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api.api-ninjas.com/v1/animals"
API_KEY = os.getenv("API_KEY")


def fetch_data(animal_name):
    """Fetches animal data from the API Ninjas Animals API."""
    headers = {"X-Api-Key": API_KEY}
    params = {"name": animal_name}
    response = requests.get(API_URL, headers=headers, params=params)
    return response.json()


def serialize_animal(animal_obj):
    """ Serializes a single animal object into an HTML card """
    name = animal_obj["name"]
    diet = animal_obj["characteristics"]["diet"]
    location = animal_obj["locations"][0]

    output = '<li class="cards__item">\n'
    output += f'  <div class="card__title">{name}</div>\n'
    output += '  <p class="card__text">\n'
    output += f'    <strong>Diet:</strong> {diet}<br/>\n'
    output += f'    <strong>Location:</strong> {location}<br/>\n'
    if "type" in animal_obj["characteristics"]:
        animal_type = animal_obj["characteristics"]["type"]
        output += f'    <strong>Type:</strong> {animal_type}<br/>\n'
    output += '  </p>\n'
    output += '</li>\n'
    return output


def main():
    animal_name = input("Enter a name of an animal: ")
    animals_data = fetch_data(animal_name)

    if animals_data:
        output = ""
        for animal in animals_data:
            output += serialize_animal(animal)
    else:
        output = f'<h2>The animal "{animal_name}" doesn\'t exist.</h2>'

    with open("animals_template.html", "r") as handle:
        template = handle.read()

    final_html = template.replace("__REPLACE_ANIMALS_INFO__", output)

    with open("animals.html", "w") as handle:
        handle.write(final_html)

    print("Website was successfully generated to the file animals.html.")


if __name__ == "__main__":
    main()