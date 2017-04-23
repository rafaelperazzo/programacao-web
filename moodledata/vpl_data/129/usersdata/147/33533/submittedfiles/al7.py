# -*- coding: utf-8 -*-
n=int(input('digite n:'))
contador=1
soma=0
while cont<n:
    if n%cont==0:
        print(cont)
        soma= soma+contador
        contador= contador+1
    else:
        contador= contador+1
if soma==n:
    print('PERFEITO')
else: print('NÃO PERFEITO')