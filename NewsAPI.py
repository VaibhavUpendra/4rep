import requests
import os
from dotenv import load_dotenv
load_dotenv()

password=os.getenv('PASSWORD')
def get_news(from_date, to_date, api_key):
    url = f"https://newsapi.org/v2/everything?qInTitle=stock%20market&from={from_date}&to={to_date}&sortBy=popularity&language=en&apiKey={api_key}"
    request = requests.get(url)
    content = request.json()
    print(content)

get_news("20-09-2024","22-09-2024",password)