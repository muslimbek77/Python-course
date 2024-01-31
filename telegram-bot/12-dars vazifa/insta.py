import requests
url = "https://instagram-downloader.p.rapidapi.com/index"

def insta_save(link):
    querystring = {"url":"https://www.instagram.com/p/CboPHrYIFti/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA=="}


    headers = {
        "X-RapidAPI-Key": "90de015fedmsh6cb4b8ec8899b66p10b5c6jsn95e5205d74bc",
        "X-RapidAPI-Host": "instagram-downloader.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    print(response.json())

insta_save("af")