import requests

response = requests.get("https://cataas.com/cat")

file = response.content

with open("pishak.png","wb") as pishak:
    pishak.write(file)