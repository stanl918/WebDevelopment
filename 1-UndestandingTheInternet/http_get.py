import requests as r

response = r.get("https://prendan-el-server.online/jonathan/Lab4/api/videogames")
response.raise_for_status()
data = response.json()

print(data)