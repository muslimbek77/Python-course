import requests
from pprint import pprint 
url = "https://instagram-media-downloader.p.rapidapi.com/rapid/post_v2.php"

def insta_save(link):

    querystring = {"url":link}

    headers = {
        "X-RapidAPI-Key": "90de015fedmsh6cb4b8ec8899b66p10b5c6jsn95e5205d74bc",
        "X-RapidAPI-Host": "instagram-media-downloader.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    try:
        result = ("video",response.json()["items"][0]["video_versions"][0]["url"])
    except:
        result = ("rasm",response.json()["items"][0]["image_versions2"]["candidates"][0]["url"])
    
    return result
    

# insta_save("https://www.instagram.com/p/CboPHrYIFti/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==")