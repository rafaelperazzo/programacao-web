# -*- coding: utf-8 -*-
import math

#COMECE SEU CÓDIGO ABAIXO DESTA LINHA
a = int(input('digite o valor da primeira carta: '))
b = int(input('digite o valor da segunda carta: '))
c = int(input('digite o valor da terceira carta: '))
d = int(input('digite o valor da quarta carta: '))
e = int(input('digite o valor da quinta carta: '))
if a<b and b<c and c<d and d<e:
    print('C')
elif a>b and b>c and c>d and d>e:
    print('D')
else:
    print('N')

