import requests
import re

url = "https://en.wikipedia.org/wiki/Internet_of_things"

# 웹 페이지의 HTML 소스 가져오기
response = requests.get(url)
html_source = response.text
# print(html_source)

# IoT 찾기
IoTs = re.findall(r"[iI][oO][tT]\w+", html_source)

# 결과 출력
print(IoTs)