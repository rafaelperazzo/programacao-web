# -*- coding: utf-8 -*-
import math

#COMECE SEU CÓDIGO ABAIXO DESTA LINHA
a=int(input('digite o valor da primeira carta entre 1 e 13: '))
b=int(input('digite o valor da segunda carta entre 1 e 13: '))
c=int(input('digite o valor da terceira carta entre 1 e 13: '))
d=int(input('digite o valor da quarta carta entre 1 e 13: '))
e=int(input('digite o valor da quinta carta entre 1 e 13: '))
f=int(input('digite o valor da sexta carta entre 1 e 13: '))
if a<b and a<c and a<d and a<e and a<f and b<c and b<d and b<e and b<f and c<d and c<e and c<f and d<e and d<f and e<f:
    print('C')
elif a>b and a>c and a>d and a>e and a>f and b>c and b>d and b>e and b>f and c>d and c>e and c>f and d>e and d>f and e>f:
    print('D')
else:
    print('N')

