# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
a=int(input('digite :'))
soma=0
for i in range(1,a,1):
    if a%i==0:
        soma=soma+i
if soma==a:
    print('perfeito')
else:
    print('nao perfeito')