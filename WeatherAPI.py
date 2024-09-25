import requests

def get_weather(city, api_key, units):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}"
    request = requests.get(url)
    content = request.json()
    print(content)

get_weather("Kannur","85da8253b69657ab26d607bb97624074","standard")

