# -*- coding: utf-8 -*-

n=int(input('Digite n: '))
numero=n
while (n>0):
    numero=numero%2
    n=n//10
    print(numero)
