# -*- coding: utf-8 -*-
a=float(input('digite a:'))
b=float(input('digite b:'))
c=float(input('digite c:'))
if c<=a and c<=b:
    print('o valor é %d'%c)
    if b<=a:
        print('o valor é %d'%b)
        print('o valor é %d'%a)
    else:
        print('o valor é %d'%a)
        print('o valor é %d'%b)
elif b<=a and b<=c:
    print('o valor é %d'%b)
    if a<=c:
        print('o valor é %d'%a)
        print('o valor é %d'%c)
    else:
        print('o valor é %d'%c)
        print('o valor é %d'%a)
else:
    print('o valor é %d'%a)
    if b<=c:
        print('o valor é %d'%b)
        print('o valor é %d'%c)
    else:
        print('o valor é %d'%c)
        print('o valor é %d'%b)
            
