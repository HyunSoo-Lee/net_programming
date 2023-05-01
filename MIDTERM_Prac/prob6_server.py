#20201514 이현수
from socket import *
import random

BUFF_SIZE = 1024
port = 7777
s_sock = socket(AF_INET, SOCK_DGRAM)
s_sock.bind(('', port))
print('Listening...')

while True:
    data, addr = s_sock.recvfrom(BUFF_SIZE)
    i = random.randint(1, 10)
    if data.decode() != 'Ping':
        print('It isn\'t ping')
        continue
    if i <= 4: # 40% 데이터 손실
        print('Packet from {} lost!'.format(addr))
        continue
    print('Packet is {} from {}'.format(data.decode(), addr))
    s_sock.sendto('Pong'.encode(), addr)