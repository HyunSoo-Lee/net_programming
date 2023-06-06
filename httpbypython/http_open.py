from urllib import parse, request

query = {'temperature': '25', 'humidity': '60'}

# urlencode 딕셔너리 -> url 쿼리 형태로 변환
encoded_query = parse.urlencode(query)

url = 'http://localhost:8080/'
get_url = url + '?' + encoded_query

#GET
rsp = request.urlopen(get_url)
print(rsp.read().decode())

#POST
rsp = request.urlopen(url, encoded_query.encode()) 
print(rsp.read().decode())