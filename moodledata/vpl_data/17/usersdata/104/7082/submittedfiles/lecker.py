# -*- coding: utf-8 -*-
from __future__ import division
import math
#ENTRADA
a=input('Digite o valor de a:')
b=input('Digite o valor de b:')
c=input('Digite o valor de c:')
d=input('Digite o valor de d:')
#PROCESSAMENTO
if a>b<c<=d:
    print('S')
elif a>b>=c>=d:
    print('S')
elif a<b>c<=d or a<b>c>=d:
    if b>d:
        print('S')
    else:
        print('N')
elif a<=b<c>d:
    print('S')
elif a<=b<=c<d:
    print('S')
else:
    print('N')
    
