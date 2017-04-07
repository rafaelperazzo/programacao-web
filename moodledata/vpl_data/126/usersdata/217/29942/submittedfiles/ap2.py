# -*- coding: utf-8 -*-
a=float(input('digite um valor a:'))
b=float(input('digite um valor b:'))
c=float(input('digite um valor c:'))
d=float(input('digite um valor d:'))
if a>=b and a>=c and a>=d:
    print('%.d'%a)
elif b>=a and b>=c and b>=d:
    print('%.d'%b)
elif c>=a and c>=b and c>=d:
    print('%.d'%c)
elif d>=a and d>=b and d>=c:
    print('%.d'%d)
if a<=b and a<=c and a<=d:
    print('%.d'%a)
elif b<=a and b<=c and b<=d:
    print('%.d'%b)
elif c<=a and c<=b and c<=d:
    print('%.d'%c)
elif d<=a and d<=b and d<=c:
    print('%.d'%d)