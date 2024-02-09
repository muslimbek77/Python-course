import requests
import random

def art_image():

    object_id = random.randint(100,1000)

    url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{object_id}"

    response = requests.get(url)

    if response.status_code == 200:
        image = response.json()["primaryImage"]
        culture = response.json()["culture"]
        museum = response.json()["repository"]

        data = {}
        data["image"] = image
        data["culture"] = culture
        data["museum"] = museum

        return data

