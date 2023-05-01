#20201514 이현수
str = 'https://serch.daum.net/search?w=tot&q=bigdata'

lst = str.split('?')
#print(lst)

spllst = lst[1].split('&')
#print(spllst)

x = []
for i in range(2):
    x.append(spllst[i].split('='))
#print(x)

answer = dict()
for i in range(2):
    answer[x[i][0]] = x[i][1]
print(answer)

answer['q'] = 'iot'
print(answer)