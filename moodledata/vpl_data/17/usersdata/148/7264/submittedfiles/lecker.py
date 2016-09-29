# -*- coding: utf-8 -*-
from __future__ import division
import math
#ENTRADA
a= input('Digite um valor para a:')
b= input('Digite um valor para b:')
c= input('Digite um valor para c:')
d= input('Digite um valor para d:')
#PROCESSAMENTO
if a>b and b>=c and c>=d :
    print('S')
elif a==b and b==c and c==d :
    print('N')
elif a<b and b>c and c>=d :
    print('S')
elif a<=b and b<c and c>d :
    print('S')
elif a<=b and b<=c and c<d :
    print('S')
else:
    print('N')
    