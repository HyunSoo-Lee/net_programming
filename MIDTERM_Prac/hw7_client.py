from socket import *
import random

port = 3333
BUFFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)

while True:
    #선송신 - 송신 파트
    msg = input('-> ')
    reTx = 0
    #송신 5번 전송
    while reTx <= 5:
        text = str(reTx) + ' ' + msg
        sock.sendto(text.encode(), ('localhost', port))
        sock.settimeout(2)

        try:
            data, addr = sock.recvfrom(BUFFSIZE)
        except timeout:
            #재전송 카운트
            reTx += 1
            continue
        else:
            break
    
    #5번 재전송 다 안된경우
    if reTx > 5:
        sock.sendto(b'fail', ('localhost', port))
        sock.settimeout(None) #잘못된거 보내야하니까 무조건 연결...!
        while True:
            try:
                nack_data, nack_addr = sock.recvfrom(BUFFSIZE)
            except timeout:
                break
            if(nack_data.decode() == 'nack'):
                print('nack :(')
                break

    #수신 파트
    sock.settimeout(None) # socket의 블로킹 모드 timeout 설정
    while True: # None인 경우, 무한정 블로킹 됨
        data, addr = sock.recvfrom(BUFFSIZE) 
        if data.decode() == 'fail':
            sock.sendto(b'nack', ('localhost', port))
            break

        elif random.random() <= 0.5:
            continue
        
        else:
            sock.sendto(b'ack', addr)
            print('<- ', data.decode())
            break
