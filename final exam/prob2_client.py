from socket import *
import random

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 7777))

while True : 
    port = input('Enter the device ID or quit : ')
    if port == 'quit':
        s.send(port.endcode())
    port = int(port)
    temp = random.randint(0,40)
    response = str(port) + ' ' + str(temp)
    print(response)
    s.send(response.encode())