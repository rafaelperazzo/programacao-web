# -*- coding: utf-8 -*-
n=int(input('digite o valor de n:'))
j=0
soma=0
if n<0:
    n=n*(-1)

for i in range(1,n+1,1):
    s=i/(n-j)
    soma=soma+s
    j=j+1

print(soma)