from socket import *

port = 3333
BUFFSIZE = 1024
sock = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('-> ')
    sock.sendto(msg.encode(), ('localhost', port))
    data, addr = sock.recvfrom(BUFFSIZE)
    print('<- ', data.decode())