# -*- coding: utf-8 -*-
from __future__ import division
import math

a= input('Insira um valor para a:')
b= input('Insira um valor para b:')
c= input('Insira um valor para c:')
d= input('Insira um valor para d:')

if a>b and b<=c and c<=d:
    print('S')
elif b>c and b>a and c<=d:
    print('S')
elif c>b and c>d and a<=b:
    print('S')
elif d>c and b>=c and a<=b:
    print('S')
else:
    print('N')