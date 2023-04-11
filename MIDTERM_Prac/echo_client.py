import socket

port = int(input("Port No: "))
address = ("localhost", port)
BUFSIZE = 1024

#주소 유형, 소켓 타입
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#서버에 연결 요청
s.connect(address)

while True:
    msg = input("Message to send: ")
    s.send(msg.encode()) #send a message to server
    data = s.recv(BUFSIZE) #receive message from server
    print("Received message: %s" % data.decode())
s.close()