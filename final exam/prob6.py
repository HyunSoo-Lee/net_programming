import requests

url = 'https://httpbin.org/post'
data = {
    'ID': '20201514',
    'Name': 'LeeHyunSoo',
    'Department': 'IoT'
    }

rsp = requests.post(url, json=data)
print(rsp.text)
print(rsp.json()['json'])