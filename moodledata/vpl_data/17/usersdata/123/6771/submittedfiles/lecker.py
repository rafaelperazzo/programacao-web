# -*- coding: utf-8 -*-
from __future__ import division
import math

a= input('Insira um valor para a:')
b= input('Insira um valor para b:')
c= input('Insira um valor para c:')
d= input('Insira um valor para d:')

if a>b and b>c and c>d:
    print('S')
elif a<b and b<c and c<d:
    print('S')
elif a<b and b>c and c>d:
    print('S')
elif a<b and b<c and c>d:
    print('S')
else:
    print('N')