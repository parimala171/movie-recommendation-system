import requests
import time

movies = ["Avatar", "Titanic", "Batman", "Inception"]

for movie in movies:
    data = {"movie": movie}

    try:
        res = requests.post("http://127.0.0.1:5007/recommend", json=data)
        print(res.json())
    except:
        print("API not running")

    time.sleep(2)