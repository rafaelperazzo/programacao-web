# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
a=int(input('digite :'))
soma=0
i=2
while i<a:
    if a%i==0:
        soma=soma+i
    i=i+1
if soma==a:
    print('perfeito')
else:
    print('nao perfeito')