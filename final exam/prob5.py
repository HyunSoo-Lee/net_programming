from urllib import parse
from urllib import request
import requests

url = 'https://search.naver.com/search.naver?query=iot'

#A
parsed_url = parse.urlparse(url)
print(parsed_url)

#B
basic_url = parsed_url[0] + '://' + parsed_url[1]
url = parse.urljoin(basic_url, parsed_url[2]) 
print(url)

#C
unparsed_url = parsed_url.geturl()
rsp = requests.get(unparsed_url)
print(rsp.headers)