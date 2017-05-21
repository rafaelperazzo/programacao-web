# -*- coding: utf-8 -*-
n=float(input('Informe um número: '))
n = int(n)

contador=0

while n>0:
    n=n//10
    contador=contador+1
print(contador)