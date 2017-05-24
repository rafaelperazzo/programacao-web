# -*- coding: utf-8 -*-
import math

#COMECE SEU CÓDIGO ABAIXO DESTA LINHA

a=int(input('digite o numero da primeira carta:'))
b=int(input('digite o numero da segunda carta:'))
c=int(input('digite o numero da terceira carta:'))
d=int(input('digite o numero da quarta carta:'))
e=int(input('digite o numero da quinta carta:'))

if a>b>c>d>e:
    print('D')
elif a<b<c<d<e:
    print('C')
else:
    print('N')