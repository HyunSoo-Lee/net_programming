from socket import *

port = 2500
BUFSIZE = 1024

#주소 유형, 소켓 타입
#_STREAM : TCP 사용
#_DGRAM : UDP 사용
sock = socket(AF_INET, SOCK_STREAM)

#종단점(address, port num)을 소켓과 결합
sock.bind(('', port))

#클라이언트 연결 대기
sock.listen(1)

#클라이언트 연결 수용
conn, (remotehost, remoteport) = sock.accept()
print('connected by', remotehost, remoteport)

while True:
    data = conn.recv(BUFSIZE)
    print("Received message: ", data.decode())
    conn.send(data)

conn.close()
sock.close()