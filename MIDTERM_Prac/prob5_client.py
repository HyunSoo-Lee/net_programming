#20201514 이현수
from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost',8888))

while True : 
    data = []
    num = input('Enter the number : ')
    
    if num == '1':
        s.send(b'1')
        for i in range(3):
            data.append(int.from_bytes(s.recv(1024), 'big'))
        print(f'Temp={data[0]}, Humid={data[1]}, Lumi={data[2]}')
    
    elif num == '2':
        s.send(b'2')
        for i in range(3):
            data.append(int.from_bytes(s.recv(1024), 'big'))
        print(f'Temp={data[0]}, Humid={data[1]}, Lumi={data[2]}')

    elif num == '3':
        s.send(b'3')
        for i in range(3):
            data.append(int.from_bytes(s.recv(1024), 'big'))
        print(f'Temp={data[0]}, Humid={data[1]}, Lumi={data[2]}')

    else:
        print('You write wrong snumber')
        s.close()