# -*- coding: utf-8 -*-
n=int(input('Quantidade de divisores a serem mostrados:'))
a=int(input('Número 1:'))
b=int(input('Número 2:'))  
x=1
for termo in range(1,n+1,1):
    if x%a==0 or x%b==0:
    x=x+1
    print(x)
