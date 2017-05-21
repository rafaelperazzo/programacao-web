# -*- coding: utf-8 -*-
n=int(input('Número de pessoas:'))
h=int(input('Instante em que passou:'))
a=h
cont=10
for i in range (2,n+1,1):
    t=int(input('Instante em que passou:'))
    b=(t-a)
    cont=cont+b
    a=t
print(cont)