# -*- coding: utf-8 -*-
from __future__ import division

p = input('')
q = input('')

i = 10

if p==q:
    print('S')

while p>=i:
    p1 = p/i
    p2 = p1//1
    p3 = p1-p2
    n = p3*i
    p = p-n
    if q==n:
        print('S')
    i = i*10
    else:
        print('N')
    