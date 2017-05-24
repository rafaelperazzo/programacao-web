# -*- coding: utf-8 -*-
import math
a=int(input('digite a:'))
b=int(input('digite b:'))
c=int(input('digite c:'))
d=int(input('digite d:'))
if a==b or b==c or c==d:
    print('F')
else:
    if a==c or b==d:
    print('V')