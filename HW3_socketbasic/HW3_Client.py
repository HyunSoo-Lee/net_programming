import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost',9000)
sock.connect(addr)

#첫번째 msg 수신
msg = sock.recv(1024)
print(msg.decode())

#학생 이름 전송
sock.send(b'HyunSoo Lee')

#학번 수신
StuId = sock.recv(1024)
print(int.from_bytes(StuId, 'big'))

sock.close()