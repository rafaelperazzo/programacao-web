# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO ABAIXO DESTA LINHA
c1=int(input('carta 1:'))
c2=int(input('carta 2:'))
c3=int(input('carta 3:'))
c4=int(input('carta 4:'))
c5=int(input('carta 5:'))

if c1<c2<c3<c4<c5:
    print ('C')
else c1>c2>c3>c4>c5:
    print ('D')
else:
    print ('N')



