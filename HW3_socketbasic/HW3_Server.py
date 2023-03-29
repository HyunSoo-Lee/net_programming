import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',9000))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Connetion from ', addr)
    #첫번째 msg 전송
    client.send(b'Hello ' + addr[0].encode())

    #학생 이름 수신
    StuName = client.recv(1024)
    print(StuName.decode())
    
    #학번 전송
    StuId = 20201514
    StuId = StuId.to_bytes(4,'big')
    client.send(StuId)

    client.close()