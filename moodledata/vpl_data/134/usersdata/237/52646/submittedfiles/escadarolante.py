# -*- coding: utf-8 -*-
n=int(input("Numero de pessoas: "))
x=int(input("Instantw em que passou: "))
a=x
contador=10
for i in range(2,n+1,1):
    t=int(input("Instante em que passou: "))
    b=(t-a)
    contador=contador+b
    a=t
print(contador)