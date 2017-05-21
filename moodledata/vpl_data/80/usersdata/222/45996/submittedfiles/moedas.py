# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('Digite o valor de uma moeda:'))
b=int(input('Digite o valor de uma moeda:'))
c=int(input('Digite o valor da cédula:'))
possivel=false
na=0
while na<=c//a and not possivel:
    nb=(c-na*a)//b
    if na*a+nb*b==c:
        possivel = verdadeiro
    else:
        na+=1
if possivel:
    print('%d moeda(s) de %d e %d moeda(s) de %d' %(na,a,nb,b))
else:
    print('Não é possível trocar a cédula')