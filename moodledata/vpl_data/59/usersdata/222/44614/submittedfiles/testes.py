# -*- coding: utf-8 -*-
n=int(input('digite n: '))
atual=int(input('digite o número: '))
cont=1
for i in range (2,n+1,1):
    proximo=int(input('digite o número: '))
    if atual!=proximo:
        cont= cont+1
    atual=proximo
print(cont)