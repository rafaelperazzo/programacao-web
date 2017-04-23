# -*- coding: utf-8 -*-
import math
a=int(input('digite a:'))
b=int(input('digite b:'))
c=int(input('digite c:'))
d=int(input('digite d:'))
if a<b<c<d or a<=b<=c<d:
    print('S')
elif a<b>c==d:
    print('S')
elif a<=b>=c>d:
    print('S')
elif a<b<c>d:
    print('S')
elif a<b<c<=d:
    print('S')
else:
    print('N')