import requests

url = "https://raw.githubusercontent.com/achintha-cccc/Hello-python/main/hello.py"
response = requests.get(url)

print(response.text)
