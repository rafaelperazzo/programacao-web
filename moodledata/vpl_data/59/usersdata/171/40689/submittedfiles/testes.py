# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
a=int(input('digite :'))
soma=0
i=0
while i<a:
    if a%i==0:
        soma=soma+1
    i=i+1
if soma==0:
    print('perfeito')
else:
    print('nao perfeito')