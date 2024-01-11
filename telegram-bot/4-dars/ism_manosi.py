from bs4 import BeautifulSoup
import requests

link = "https://ismlar.com/uz/name/Muhammad"

content = requests.get(link).content

soup = BeautifulSoup(content,"html5lib")
soup = soup.find("div",class_ = "p-4 rounded-2xl mb-4 space-y-4 bg-cyan-100").find("p")
print(soup.text.strip())
