str = 'Hello, IoT'

print(len(str))
print(str *5)
print(str[:3])
print(str[-3:])
print(str.upper())
print('\n\n')

lst = ['H', 'e', 'l', 'l', 'o', ',', ' ', 'I', 'o', 'T']
lst.append('!')
print(lst)
del lst[4]
print(lst)
lst.insert(4, 'a')
print(lst)
print(''.join(lst))
print(lst)
lst.sort(reverse=True)
print(lst)
print('\n\n')

str = 'https://search.naver.com/search.naver?where=nexearch&ie=utf8&query=iot'
#{'where':'nexearch', 'ie':'utf8', 'query':'iot'}

lst = str.split('?')
print(lst)

spllst = lst[1].split('&')
print(spllst)

x = []
for i in range(3):
    x.append(spllst[i].split('='))
print(x)

answer = dict()
for i in range(3):
    answer[x[i][0]] = x[i][1]
print(answer)
print('\n\n')



class MyComplex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

def Calculator(complex1, complex2):
    a = complex1.real
    b = complex1.imaginary
    c = complex2.real
    d = complex2.imaginary
    real_cal = a*c - b*d
    imag_cal = a*d + b*c
    result = f'{real_cal} + {imag_cal}i' 
    return  result

complex_1 = MyComplex(3, -4)
complex_2 = MyComplex(-5,2)
print(Calculator(complex_1, complex_2))
print('\n\n')

import struct


data = 1234
print(data)
data = struct.pack('i', data)
print(data)
data = struct.unpack('i', data)
print(data)
print(type(data))
print(data[0])

print('0xffff')
x = 0xFFFF
print(type(x))
print(x)