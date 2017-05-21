# -*- coding: utf-8 -*-
n= float(input('Digite o número inteiro:'))
n=n//1

cont=0
while n>0:
    n=n//10
    cont=cont+1
print (cont)

