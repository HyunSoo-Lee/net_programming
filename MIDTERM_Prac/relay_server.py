from socket import *

# rel_s= socket(AF_INET, SOCK_STREAM)
# rel_s.bind(('', 9000))
# rel_s.listen(10)

while True:
    # 릴레이 서버 소켓 생성 및 연결 대기
    rel_s= socket(AF_INET, SOCK_STREAM)
    rel_s.bind(('', 9000))
    rel_s.listen(10)

    # 브라우저로부터 HTTP 요청 메시지 수신
    rel_c, addr = rel_s.accept()
    data = rel_c.recv(1024)
    msg = data.decode()

    # 요청 라인과 host 헤더 추출
    reg = msg.split('\r\n')[0]
    print(reg)
    hostmeg = 'Host: www.daum.net'

    # 외부 서버로 HTTP 요청 메시지 전송
    ext_s = socket(AF_INET, SOCK_STREAM)
    ext_s.connect(('www.daum.net', 80))
    ext_s.send(reg.encode() +b'\r\n'+ hostmeg.encode() +b'\r\n\r\n')

    # 외부 서버로부터 HTTP 응답 메시지 수진 및 릴레이 -> 브라우저
    web_data = ext_s.recv(1024)
    rel_c.sendall(web_data)

    # 소켓 종료
    rel_s.close()
    ext_s.close()
