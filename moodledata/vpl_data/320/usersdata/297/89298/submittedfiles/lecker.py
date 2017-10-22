# -*- coding: utf-8 -*-
import math
a=int(input(' '))
b=int(input(' '))
c=int(input(' '))
d=int(input(' '))
if a>b>=c>=d or a<b>c>=d or a<=b<c>d  or a<=b<=c<d or a=b=c>d or (a=c=d)>b or (a=b=d)>c or (b=c=d)>a:
    print('S')
else :
    print('N')