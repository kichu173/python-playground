# pip install requests

import requests

params = { # dictionary
    "name": "Kiran",
    "age": 28,
}

response = requests.get("https://httpbin.org/get", params=params)
print(response.url)

# print(response.text)
res_json = response.json()

del res_json['origin']
print(res_json)

# print(response.status_code)

print("----------")

payload = {
    "name": "Mike",
    "age": 25,
}

response1 = requests.post("https://httpbin.org/post", data=payload)

print(response1.json())

print("----------")

response2 = requests.get("https://httpbin.org/status/404")

if response2.status_code == requests.codes.not_found:
    print("The page was not found")
else:
    print(response2.status_code)

print("----------")

response3 = requests.get("https://httpbin.org/user-agent")

print(response3.text)

headers = {
    "User-Agent": "Kiran/1.1"
}

response4 = requests.get("https://httpbin.org/user-agent", headers=headers)

print(response4.text)

headers = {
    "User-Agent": "Kiran/1.1",
    "Accept": "image/png"
}

response5 = requests.get("https://httpbin.org/image", headers=headers)

with open("myimage.png", "wb") as f:
    f.write(response5.content)

print("----------")

response6 = requests.get("https://httpbin.org/delay/5", timeout=3)

print(response6)