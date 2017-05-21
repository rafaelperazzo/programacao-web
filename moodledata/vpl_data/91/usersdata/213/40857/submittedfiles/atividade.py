# -*- coding: utf-8 -*-
n=int(input('Informe um número: '))

contador=0

while n>0:
    n=n//10
    contador=contador+1
print(contador)