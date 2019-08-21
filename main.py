import requests
response = requests.get("https://habr.com/ru/")
with open("data.html","w",encoding="utf-8")as file:
    file.write(response.text)