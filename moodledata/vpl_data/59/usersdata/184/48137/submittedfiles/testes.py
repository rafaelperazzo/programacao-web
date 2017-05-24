# -*- coding: utf-8 -*-
a=float(input('digite a:'))
b=float(input('digite b:'))
c=float(input('digite c:'))
if a>=b and a>=c:
    print('%d'%a)
elif b>=a and b>=c:
    print('%d'%b)
elif c>=a and c>=b:
    print('%d'%c)
    else:
        if a==b==c:
            print('iguais')