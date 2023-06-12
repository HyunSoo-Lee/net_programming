from socket import *
import sys
import time

BUF_SIZE = 1024
LENGTH = 4  # '파일 크기': 4바이트

s = socket(AF_INET, SOCK_STREAM)
while True : 
    port = input('Enter the device number or quit : ')
    port = int(port)
    if port == 1 or 2:
        s.connect(('localhost', 9999))
    else:
        print('You write wrong device number')
        s.close()
    s.send(port.to_bytes(4,'big'))
    
    result = s.recv(1024)
    print(result.decode())

    s.close()
    s = socket(AF_INET, SOCK_STREAM)