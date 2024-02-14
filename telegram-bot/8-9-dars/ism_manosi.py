from bs4 import BeautifulSoup
import requests

def ismlar_manosi(ism):
  link = f"https://ismlar.com/uz/name/{ism}"
  content = requests.get(link).content
  soup = BeautifulSoup(content,"html5lib")
  try:                            
    soup = soup.find("div",class_ = "p-4 rounded-2xl mb-4 space-y-4 bg-cyan-100").find("p").text
  except:
    try:
      soup = soup.find("div",class_ = "p-4 rounded-2xl mb-4 space-y-4 bg-pink-100").find("p").text
    except:
      return "topilmadi"
  return soup.strip()

natija = ismlar_manosi("Sardor")
print(natija)
