# -*- coding: utf-8 -*-
import math

#COMECE SEU CÓDIGO ABAIXO DESTA LINHA
a=int(input('digite o valor da primeira carta: '))
b=int(input('digite o valor da segunda carta: '))
c=int(input('digite o valor da terceira carta: '))
d=int(input('digite o valor da quarta carta: '))
e=int(input('digite o valor da quinta carta: '))
f=int(input('digite o valor da sexta carta: '))
if a<b and a<c and a<d and a<e and a<f and b<c and b<d and b<e and b<f and c<d and c<e and c<f and d<e and d<f and e<f:
    print('C')
elif a>b and a>c and a>d and a>e and a>f and b>c and b>d and b>e and b>f and c>d and c>e and c>f and d>e and d>f and e>f:
    print('D')
else:
    print('N')

