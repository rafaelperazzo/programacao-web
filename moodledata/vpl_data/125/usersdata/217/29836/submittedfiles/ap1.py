# -*- coding: utf-8 -*-
a=float(input('digite um valor a'))
b=float(input('digite um valor b'))
c=float(input('digite um valor c'))
if a>=b and a>=c:
    if b>=c:
        print('%.d'%c)
        print('%.d'%b)
        print('%.d'%a)
    else:
        print('%.d'%b)
        print('%.d'%c)
        print('%.d'%a)
elif b>=a and b>=c:
    if a>=c:
        print('%.d'%c)
        print('%.d'%a)
        print('%.d'%b)
    else:
        print('%.d'%a)
        print('%.d'%c)
        print('%.d'%b)
else:
    if a>=b:
        print('%.d'%b)
        print('%.d'%a)
        print('%.d'%c)
    else:
        print('%.d'%a)
        print('%.d'%b)
        print('%.d'%c)
    