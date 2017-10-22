# -*- coding: utf-8 -*-
import math

#COMECE SEU CÓDIGO ABAIXO DESTA LINHA

a=int(input('Digite o valor da primeira carta: '))
b=int(input('Digite o valor da segunda carta: '))
c=int(input('Digite o valor da terceira carta: '))
d=int(input('Digite o valor da quarta carta: '))
e=int(input('Digite o valor da quinta carta: '))
cont=0

if (a>b>c>d>e):
    print('D')
    cont=cont+1
if (a<b<c<d<e):
    print('C')
    cont=cont+1
if (cont==0):
    print('N')




