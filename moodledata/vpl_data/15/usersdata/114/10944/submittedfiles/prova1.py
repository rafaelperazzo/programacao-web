# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO ABAIXO DESTA LINHA
a=input('valor entre 1 e 13 para essa carta: ')
b=input('valor entre 1 e 13 para essa carta: ')
c=input('valor entre 1 e 13 para essa carta: ')
d=input('valor entre 1 e 13 para essa carta: ')
e=input('valor entre 1 e 13 para essa carta: ')

if a>b>c>d>e:
    print ('D')
elif a<b<c<d<e:
    print ('C')
else:
    print ('N')


