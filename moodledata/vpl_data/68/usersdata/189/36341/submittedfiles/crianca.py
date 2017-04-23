# -*- coding: utf-8 -*-
p1=int(input('digite o p1:'))
c1=int(input('digite o c1:'))
p2=int(input('digite o p2:'))
c2=int(input('digite o c2:'))
if p1*c1==p2*c2:
    print('0')
elif p1*c1>p2*c2:
    print('-1')
else:
    print('1')