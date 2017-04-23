# -*- coding: utf-8 -*-
n=int(input('digite n:'))
cont=1
soma=0
while cont<n:
    if n%cont==0:
        soma= soma+cont
        cont= cont+1
        print(cont)
    else:
        cont= cont+1
if soma==n:
    print('PERFEITO')
else: print('NÃO PERFEITO')