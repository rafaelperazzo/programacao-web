# -*- coding: utf-8 -*-
n=int(input('digite n:'))
m=int(input('digite m:'))
cont=0
for i in range (1,n+1,1):
    a=int(input('digite pontos 1:'))
    b=int(input('digite pontos 2:'))
    soma=a+b
    if soma>=m:
        cont=cont+1
print(cont)
        