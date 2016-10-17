# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO ABAIXO DESTA LINHA
#ENTRADA
c1=int(input('digite o valor da carta 1:'))
c2=int(input('digite o valor da carta 2:'))
c3=int(input('digite o valor da carta 3:'))
c4=int(input('digite o valor da carta 4:'))
c5=int(input('digite o valor da carta 5:'))

#SAIDA
if c1<c2<c3<c4<c5:
    print ('C')
elif c1>c2>c3>c4>c5:
    print ('D')
else:
    ('N')


