import requests

url = "https://tiktok-download-video1.p.rapidapi.com/getVideo"

querystring = {"url":"https://www.tiktok.com/@tiktok/video/7106658991907802411","hd":"1"}

headers = {
	"X-RapidAPI-Key": "90de015fedmsh6cb4b8ec8899b66p10b5c6jsn95e5205d74bc",
	"X-RapidAPI-Host": "tiktok-download-video1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())