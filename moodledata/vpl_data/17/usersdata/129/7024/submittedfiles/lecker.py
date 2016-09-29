# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('Digite o valor: ')
b=input('Digite o valor: ')
c=input('Digite o valor: ')
d=input('Digite o valor: ')
if a>b and a<b>c:
      print ('N')
elif a>b and b<c>d :
      print ('N')
elif a>b and c<d:
      print ('N')
elif a<b>c and b<c>d:
      print ('N')
elif a<b>c and c<d:
      print ('N')
elif b<c>d and c<d:
      print ('N')
else:
    print ('S')