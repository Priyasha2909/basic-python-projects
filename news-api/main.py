
import requests

query = input("What news buzz you want to have a look today?")
api_key = "808d3fdc817f47379280d503514fc1c1"

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-12-04&sortBy=publishedAt&apiKey={api_key}"


# Fetching the content of url
r = requests.get(url)

data = r.json()

# articles is a list of dictionaries in data
articles = data["articles"]

for index, art in enumerate(articles):
    print(index+1,art["title"], art["url"])
    print("**************************************************************************************************************************************")
