from socket import *

port = 3333
BUFFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))
# tcp와 다른점 -> connect & accept가 없음!
# sendto ~ recvfrom으로 이루어진다.

while True:
    data, addr = sock.recvfrom(BUFFSIZE)
    print('<- ', data.decode())
    resp = input('-> ')
    sock.sendto(resp.encode(), addr)