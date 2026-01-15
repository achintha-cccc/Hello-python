import requests

url = "https://raw.githubusercontent.com/%%%%/Hello-python/main/hello.py"
response = requests.get(url)

print(response.text)
