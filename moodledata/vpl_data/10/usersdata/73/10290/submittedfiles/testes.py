# -*- coding: utf-8 -*-
from __future__ import division
a=input('a')
b=input('b')
c=input('c')
if a>b and a>c:
    print ('maior:%.1f' %a)
    if b>c:
        print('intermediario:%.1f' %b)
    else:
        print('menor:%.1f' %c)
elif b>a and b>c:
    print ('maior:%.1f' %b)
    if a>c:
        print('intermediario:%.1f' %a)
    else:
        print('menor:%.1f' %c)
    
