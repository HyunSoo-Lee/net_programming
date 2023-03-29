from socket import *

def calculator(str):
    str = str.replace(" ", "")

    # 연산기호 위치 잡기
    for i in range(len(str)):
        if str[i] in "+-*/":
            operator = str[i]
            break
    
    # 숫자 분리, 형변환 -> 연산기호 있는 곳 이전까지 숫자 하나, 연산기호 있는 곳 이후부터 숫자 하나
    num1 = str[:i]
    #print(num1)
    num2 = str[i+1:]
    #print(num2)
    num1 = int(num1)
    num2 = int(num2)
    
    # 계산    
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    
    result = round(result,1)
    return result

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 3333))
s.listen(5)

print('waiting...')

while True:
    client, addr = s.accept()
    print('connection from ', addr)
    while True:
        data = client.recv(1024)
        if not data:
            break
        try:
            rsp = calculator(data.decode())
            rsp = str(rsp)
        except:
            client.send(b'Try again')
        else:
            client.send(rsp.encode())
    client.close()
