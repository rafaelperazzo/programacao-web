# -*- coding: utf-8 -*-
from __future__ import division
w=input('digite w:')
x=input('digite x:')
z=input('digite z:')
if (w>=x):
    qw=z//w
    qx=(z%w)//x
    if ((z%w)%x==0):
        print(qw)
        print(qx)
    else:
        print('N')
else:
    qx=z//x
    qw=(z%x)//w
    if ((z%x)%w==0):
        print (qw)
        print (qx)
    else:
        print('N')
        