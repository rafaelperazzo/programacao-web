# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
a=int(input('digite :'))
i=1
soma=0
while i<a:
    if a%i==0:
        soma=soma+i
    i=i+1
if soma==a:
    print('perfeito')
else:
    print('nao perfeito')