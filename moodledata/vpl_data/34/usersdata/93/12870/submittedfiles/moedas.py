# -*- coding: utf-8 -*-
from __future__ import division
a=input('a')
b=input('b')
c=input('c')
qa=0
while True:
    if (c-qa*a)%b==0:
        print(qa)
        print((c-qa*a)/b)
        break
    if c<qa*a:
        print('N')
        break

