import socket

HOST = ''  # Symbolic name meaning all available interfaces
PORT = 8080  # Arbitrary non-privileged port

def relay_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(1)
        print(f'Relay server is listening at http://localhost:{PORT}')

        while True:
            conn_browser, addr_browser = s.accept()
            with conn_browser:
                print('Connected by', addr_browser)

                # Receive request from browser
                data = conn_browser.recv(1024)
                print('Received from browser:', data)

                # Parse the request message from browser
                request = data.decode()
                request_lines = request.split('\r\n')
                request_line = request_lines[0]
                url = request_line.split(' ')[1]

                # Send request to external server
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s_server:
                    s_server.connect(('www.daum.net', 80))
                    print('Connected to www.daum.net')

                    # Modify the request message
                    modified_request = request_line + '\r\n'
                    modified_request += 'Host: www.daum.net\r\n'
                    modified_request += '\r\n'

                    # Send the modified request message to external server
                    s_server.sendall(modified_request.encode())

                    # Receive response from external server
                    response = b''
                    while True:
                        data = s_server.recv(1024)
                        if not data:
                            break
                        response += data

                    # Send the response to browser
                    conn_browser.sendall(response)

if __name__ == '__main__':
    relay_server()
