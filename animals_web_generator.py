import json


def load_data(file_path):
    """ Loads JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


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
    animals_data = load_data("animals_data.json")

    output = ""
    for animal in animals_data:
        output += serialize_animal(animal)

    with open("animals_template.html", "r") as handle:
        template = handle.read()

    final_html = template.replace("__REPLACE_ANIMALS_INFO__", output)

    with open("animals.html", "w") as handle:
        handle.write(final_html)


if __name__ == "__main__":
    main()
