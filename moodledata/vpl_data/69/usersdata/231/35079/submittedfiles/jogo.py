# -*- coding: utf-8 -*-
import math
Cv=float(input('digite Cv : '))
Ce=float(input('digite Ce : '))
Cs=float(input('digite Cs : '))
Fv=float(input('digite Fv : '))
Fe=float(input('digite Fe : '))
Fs=float(input('digite Fs : '))
a=Cv*3
b=Fv*3
c=a+Ce
d=b+Fe
if c>d:
    print('C')
elif d>c:
    print('F')
elif c==d and Cv>Fv:
    print('C')
elif c==d and Fv>Cv:
    print('F')
