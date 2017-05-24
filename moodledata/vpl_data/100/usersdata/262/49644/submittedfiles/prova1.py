# -*- coding: utf-8 -*-
import math

#COMECE SEU CÓDIGO ABAIXO DESTA LINHA

a=int(input('Digite o valor de a:'))
b=int(input('Digite o valor de b:'))
c=int(input('Digite o valor de c:'))
d=int(input('Digite o valor de d:'))
e=int(input('Digite o valor de e:'))

if (a<b) and (b<c) and (c<d) and (d<e):
    print('C')
elif (a>b) and (b>c) and (c>d) and (d>e):
    print('D')
else:
    print('N')

