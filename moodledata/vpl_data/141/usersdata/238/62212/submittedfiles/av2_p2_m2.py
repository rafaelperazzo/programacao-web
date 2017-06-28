# -*- coding: utf-8 -*-
q=int(input('digite quantidade de portas:'))
c=int(input('digite quantidade de entradas:'))
j=int(input('digite quantidade de saidas:'))
a=[]
for i in range(0,q,1):
    l=int(input('digite vida:'))
    c.append(l)
soma=0
for i in range(c,j+1,1):
    soma=soma+a[i]
print(soma)

    