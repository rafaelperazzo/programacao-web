# -*- coding: utf-8 -*-
n=int(input('digite n:'))
soma=0
contador=1
while contador<n:
    if n%contador==0:
        print(contador)
        soma= soma+contador
        contador= contador+1
    else:
        contador= contador+1
if soma==n:
    print('PERFEITO')
else: print('NÃO PERFEITO')