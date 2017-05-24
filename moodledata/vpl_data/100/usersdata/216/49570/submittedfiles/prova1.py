# -*- coding: utf-8 -*-
import math

#COMECE SEU CÓDIGO ABAIXO DESTA LINHA
a=int(input('Digite um valor:'))
b=int(input('Digite um valor:'))
c=int(input('Digite um valor:'))
d=int(input('Digite um valor:'))
e=int(input('Digite um valor:'))

if a<b and b<c and c<d and d<e:
    print('C')
elif a>b and b>c and c>d and d>e:
    print('D')
else:
    print('N')

