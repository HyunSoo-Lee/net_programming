from urllib import parse

iot_url_1 = parse.urljoin('https://home.sch.ac.kr', 'iot') 
print('IoT Homepage 1:', iot_url_1)

iot_url_2 = 'https://home.sch.ac.kr'+'/iot'
print('IoT Homepage 2:', iot_url_2)

big_url = parse.urljoin(iot_url_1, 'bigdata')
print('Bigdata Homepage:', big_url)

p_url = parse.urlparse(iot_url_1)
print('Parsed URL:', p_url)
print('Unparsed URL:', p_url.geturl())

url = parse.urlunparse(p_url)
print('Encoded:', url)