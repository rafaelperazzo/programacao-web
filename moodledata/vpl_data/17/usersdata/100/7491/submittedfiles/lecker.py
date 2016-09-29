# -*- coding: utf-8 -*-
from __future__ import division
import math
a =  int(input('Digite o valor de A:'))
b =  int(input('Digite o valor de B:'))
c =  int(input('Digite o valor de C:'))
d =  int(input('Digite o valor de D:'))
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
elif a>b and a<b>c and b<c>d :
    print ('N')
elif a>b and a<b>c and d>c :
    print ('N')
elif a<b>c and a<b>c and b<c>d:
    print ('N')
elif a==b==c==d:
    print ('N')
    
else:
    print ('S')