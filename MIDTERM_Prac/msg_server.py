import socket

# 서버 IP, PORT
HOST = 'localhost'
PORT = 9000

# Mailbox 딕셔너리
mailbox = {}

# UDP 소켓 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

while True:
    # 클라이언트로부터 메시지 수신
    data, addr = sock.recvfrom(1024)
    message = data.decode().split()

    # 메시지 분리
    command = message[0].lower()
    mboxID = message[1]
    if len(message) > 2:
        msg = ' '.join(message[2:])
    else:
        msg = ''

    # 메시지 처리
    if command == 'send':
        if mboxID not in mailbox:
            mailbox[mboxID] = []
        mailbox[mboxID].append(msg)
        sock.sendto('OK'.encode(), addr)
    elif command == 'receive':
        if mboxID in mailbox and len(mailbox[mboxID]) > 0:
            sock.sendto(mailbox[mboxID][0].encode(), addr)
            del mailbox[mboxID][0]
        else:
            sock.sendto('No messages'.encode(), addr)
    elif command == 'quit':
        break

# UDP 소켓 종료
sock.close()