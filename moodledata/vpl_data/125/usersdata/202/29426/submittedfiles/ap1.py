# -*- coding: utf-8 -*-
a=float(input('digite a:'))
b=float(input('digite b:'))
c=float(input('digite c:'))
if a<=b and a<=c:
    print ('%d'%a)
    if b<=c:
        print('%d'%b)
        print('%d'%c)
    else:
        print('%d'%c)
        print('%d'%b)
if b<=a and b<=c:
    print('%d'%b)
    if a<=c:
        print('%d'%a)
        print('%d'%c)
    else:
        print('%d'%c)
        print('%d'%a)
if c<=a and c<=b:
    print('%d'%c)
    if a<=b:
        print('%d'%a)
        print('%d'%b)
    else:
        print('%d'%b)
        print('%d'%a)
