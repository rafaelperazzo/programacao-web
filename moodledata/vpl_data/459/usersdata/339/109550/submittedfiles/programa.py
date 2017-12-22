# -*- coding: utf-8 -*-

C=int(input('Consultas: '))
e=[]
r=0
for i in range(C):
    e.append(float(input('tamanho: ')))
    r+=2
    for j in range(C):
        if e[i]==e[j]:
            r-=1
print(r)
