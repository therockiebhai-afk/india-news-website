import os
import requests

def handler(request):
    api_key = os.environ.get("NEWSDATA_API_KEY")
    url = f"https://newsdata.io/api/1/news?apikey={api_key}&country=in&language=en&category=top"
    response = requests.get(url)
    return response.json()
