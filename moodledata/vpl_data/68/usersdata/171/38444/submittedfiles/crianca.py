# -*- coding: utf-8 -*-
p1=float(input('digite o peso da criança 1:'))
p2=float(input('digite o peso da criança 2:'))
c1=float(input('digite o comprimento do lado 1 da gangorra:'))
c2=float(input('digite o comprimento do lado 2 da gangorra:'))
if p1>=p2 and c1>c2 or p1>p2 and c1>=c2:
    print('-1')
elif p1<=p2 and c1<c2 or p1<p2 and c1<=c2:
    print('1')
else:
    print('0')