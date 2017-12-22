# -*- coding: utf-8 -*-
a=[]
b=[]
n=int(input('digite a quantidade de elementos da lista a: '))
m=int(input('digite a quantidade de elementos da lista b: '))
for i in range(n):
    a.append(int(input('digite os valores da lista a')))
for i in range(m):
    b.append(int(input('digite os valores da lista b')))
repetidos=[]   
for i in b:
    if b not in a:
        repetidos.append(i)
print(repetidos)
print(len(repetidos))
        


