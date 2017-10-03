# -*- coding: utf-8 -*-
p1 = float(input('p1'))
c1 = float(input('c1'))
p2 = float(input('p2'))
c2 = float(input('c2'))
if p1*c1==p2*c2:
    print('0')
if p1*c1<p2*c2:
    print(-1)
if p1*c1>p2*c2:
    print(1)