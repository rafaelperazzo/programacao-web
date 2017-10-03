# -*- coding: utf-8 -*-
n = int(input('digite o valor de n : '))
resultado=1
lista=range(1,n-1)
for x in lista:
    resultado=x*resultado
print(n,resultado)