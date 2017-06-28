# -*- coding: utf-8 -*-
n=int(input('Quantidade de salas:'))
a=[]
for i in range(1,n+1,1):
    y=int(input('Digite o valor y:'))
    a.append(y)
x=int(input(' Y de entrada:'))
z=int(input(' Y de saída:'))
s=0
for j in range(x,z+1,1):
    s=s+a[j]
print(s)

