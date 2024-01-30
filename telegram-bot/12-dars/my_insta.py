import requests

def insta_save(link):
    url = "https://instagram-post-and-reels-downloader.p.rapidapi.com/insta/"

    querystring = {"url":link}

    headers = {
        "X-RapidAPI-Key": "90de015fedmsh6cb4b8ec8899b66p10b5c6jsn95e5205d74bc",
        "X-RapidAPI-Host": "instagram-post-and-reels-downloader.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response.json()["detail"]["data"]["items"][0]["pictureUrl"]

# print(insta_save("https://www.instagram.com/p/CxTG997oaH1/"))