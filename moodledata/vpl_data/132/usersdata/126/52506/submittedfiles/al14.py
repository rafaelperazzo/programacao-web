# -*- coding: utf-8 -*-
n=int(input('digite a quantidade de pessoas:'))
soma=0
for i in range(1,n+1,1):
    x=int(input('digite a idade da pessoa:'))
    soma=soma+x
    i=i+1
y=soma/n
print(y)