from bs4 import BeautifulSoup
import requests


def ismlar_manosi(ism):
  link = f"https://ismlar.com/uz/name/{ism}"
  content = requests.get(link).content
  soup = BeautifulSoup(content,"html5lib")
  if "404 Афсуски, сиз қидирган саҳифа топилмади."==soup.find("h1").text.strip():
    return "topilmadi"
  else:
    try:                            
      soup = soup.find("div",class_ = "p-4 rounded-2xl mb-4 space-y-4 bg-cyan-100").find("p").text
    except:
      soup = soup.find("div",class_ = "p-4 rounded-2xl mb-4 space-y-4 bg-pink-100").find("p").text
      
    return soup.strip()


