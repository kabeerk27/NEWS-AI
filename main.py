import requests
query = input("What type of news are you looking for?  ")
api = "45862a564cd24b4e82b5d984c183748d"
url = f"https://newsapi.org/v2/everything?q={query}&from=2025-07-07&sortBy=publishedAt&apiKey={api}"
print(url)
if len(api) != 32:
    print("Warning: The API key appears to be invalid (incorrect length).")
r = requests.get(url)
data = r.json()
articles = data["articles"]
for index, article in enumerate(articles):
    print(index + 1 ,article["title"], article["url"])
    print("\n********************\n")