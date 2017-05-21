# -*- coding: utf-8 -*-
n=float(input('Digite um número inteiro: '))
n=int(n)
cont=0
while (n>0):
    n=n//10
    cont=cont+1
print(cont)
