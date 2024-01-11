import requests

def get_cat(text):
    url = f"https://cataas.com/cat/says/{text}"
    
    return requests.get(url).content