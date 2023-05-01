#20201514 이현수
from socket import *
from time import *

BUFF_SIZE = 1024
port = 7777

c_sock = socket(AF_INET, SOCK_DGRAM)

while True:
    j = 0
    timeoutT = 1 # 1초
    data = input('Send Ping : ')
    while True:
        c_sock.sendto(data.encode(), ('localhost',port))
        if j ==  0:
            sendT = time()
            #print(sendT)
        c_sock.settimeout(timeoutT)
        try:
            data, addr = c_sock.recvfrom(BUFF_SIZE)
        except timeout:
            if j == 3:
                print('Fail')
                break
            j += 1
            sleep(1)
        else:
            receiveT = time()
            #print(receiveT)
            #print('Response', data.decode())
            print(f'Success (RTT: {receiveT - sendT})')
            break