# -*- coding: utf-8 -*-
a=float(input('coloque o valor de a:'))
b=float(input('coloque o valor de b:'))
c=float(input('coloque o valor de c:'))
if c<=a and c<=b:
    print('%d'%c)
    if b<=a:
        print('%d'%b)
        print('%d'%a)
    else:
        print('%d'%a)
        print('%d'%b)
elif b<=a and b<=c:
    print('%d'%b)
    if a<=c:
        print('%d'%a)
        print('%d'%c)
    else:
        print('%d'%c)
        print('%d'%a)
else:
    print('%d'%a)
    if b<=c:
        print('%d'%b)
        print('%d'%c)
    else:
        print('%d'%c)
        print('%d'%b)
    
