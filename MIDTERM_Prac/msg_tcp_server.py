import socket

# 서버 IP, PORT
HOST = 'localhost'
PORT = 9000

# Mailbox 딕셔너리
mailbox = {}

# UDP 소켓 생성
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock.bind((HOST, PORT))

# TCP 소켓 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen()

#sock close를 위한 이중 while문 break 스위치
sock_switch = False

while True:
    # 클라이언트로부터 연결 요청을 대기하고 수락
    conn, addr = sock.accept()
    print("Connected by {}".format(addr))

    while True:
        # 클라이언트로부터 메시지 수신
        # data, addr = sock.recvfrom(1024)
        data = conn.recv(1024)
        if not data:
            break

        # 메시지 분리
        message = data.decode().split()
        command = message[0].lower()
        if len(message) > 2:
            mboxID = message[1]
            msg = ' '.join(message[2:])
        else:
            msg = ''

        # 메시지 처리
        if command == 'send':
            if mboxID not in mailbox:
                mailbox[mboxID] = []
            mailbox[mboxID].append(msg)
            #sock.sendto('OK'.encode(), addr)
            conn.sendall('OK'.encode())
        elif command == 'receive':
            if mboxID in mailbox and len(mailbox[mboxID]) > 0:
                #sock.sendto(mailbox[mboxID][0].encode(), addr)
                conn.sendall(mailbox[mboxID][0].encode())
                del mailbox[mboxID][0]
            else:
                conn.sendall('No messages'.encode())
        elif command == 'quit':
            conn.close()
            sock.close()
            sock_switch = True
            break
    if sock_switch ==  True:
        break