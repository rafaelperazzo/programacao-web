# -*- coding: utf-8 -*-
import math
a=float(input('digite a:'))
b=float(input('digite b:'))
c=float(input('digite c:'))
d=float(input('digite d:'))
if a!=b!=c!=d and (a>(b+c+d) or b>(a+c+d) or c>(b+a+d) or d>(b+c+a)):
    print('S')
elif a==b and (a>(c+d) or b>(c+d)):
    print('s')
elif a==c and (a>(b+d) or c>(b+d)):
    print('s')
elif a==d and (a>(b+c) or d>(b+c)):
    print('s')
elif b==c and (b>(a+d) or c>(a+d)):
    print('s')
elif b==d and (b>(c+a) or d>(a+c)):
    print('s')
elif d==c and (c>(b+a) or d>(b+a)):
    print('s')
elif a==b==c and a>d:
    print('s')
elif b==c==d and b>a:
    print('s')
elif c==d==a and a>b:
    print('s')
elif a==b==d and a>c:
    print('s')
else: print('n')




