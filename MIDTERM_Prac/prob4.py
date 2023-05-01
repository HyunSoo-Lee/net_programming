#20201514 이현수
import socket

ip = '220.69.189.125'
port = 443

hostname = socket.gethostbyaddr(ip)
print(hostname[0])

protocol = socket.getservbyport(port)
print(protocol)

url = f'{protocol}://{hostname[0]}'
print(url)

ip_by_bytes = socket.inet_aton(ip)
print(ip_by_bytes)