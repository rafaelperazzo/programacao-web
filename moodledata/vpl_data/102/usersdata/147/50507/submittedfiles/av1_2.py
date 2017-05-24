# -*- coding: utf-8 -*-
import math
a=int(input('digite a:'))
s=int(input('digite s:'))
d=int(input('digite d:'))
w=int(input('digite w:'))
if a==d and s!=w:
    print('V')
if a==w and s!=d:
    print('F')