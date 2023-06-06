from urllib import parse

url = 'https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=iot'
#parsed_url = parse.urlparse(url)

#만약 parameter 없이 5개 요소로 반환하려면
parsed_url = parse.urlsplit(url)


print(parsed_url)
print('scheme :', parsed_url.scheme)
print('netloc :', parsed_url.netloc)
print('path :', parsed_url.path)
#urlsplit의 경우 없애야 함!
#print('params :', parsed_url.params) 
print('query :', parsed_url.query) 
print('fragment:', parsed_url.fragment)
