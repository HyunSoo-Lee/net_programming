str = 'Hello, IoT'

print(len(str))
print(str *5)
print(str[:3])
print(str[-3:])
print(str.upper())

lst = ['H', 'e', 'l', 'l', 'o', ',', ' ', 'I', 'o', 'T']
lst.append('!')
print(lst)
del lst[4]
print(lst)
lst.insert(4, 'a')
print(lst)
