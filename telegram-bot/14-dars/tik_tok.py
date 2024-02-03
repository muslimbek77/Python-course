import requests
from pprint import pprint
url = "https://tiktok-download-video1.p.rapidapi.com/getVideo"

def tiktok_save(link):
	querystring = {"url":link,"hd":"1"}

	headers = {
		"X-RapidAPI-Key": "90de015fedmsh6cb4b8ec8899b66p10b5c6jsn95e5205d74bc",
		"X-RapidAPI-Host": "tiktok-download-video1.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)
	data = {}
	try:
		data["music"] = response.json()["data"]["music"]
	except:
		pass
	try:
		data["video"] = response.json()["data"]["hdplay"]
	except:
		pass
	try:
		data["images"] = response.json()["data"]["images"]
	except:
		pass

	return data

