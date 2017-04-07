# -*- coding: utf-8 -*-
a=float(input('Digite o valor de a:'))
b=float(input('Digite o valor de b:'))
c=float(input('Digite o valor de c:'))
if c<=a and c<=b:
    print('%.2f'%c)
    if b<=a:
        print('%.2f'%b)
        print('%.2f'%a)
    else:
        print('%.2f'%a)
        print('%.2f'%b)
elif b<=a and b<=c:
    print('%.2f'%b)
    if a<=c:
        print('%.2f'%a)
        print('%.2f'%c)
    else:
        print('%.2f'%c)
        print('%.2f'%a)
else:
    print('%.2f'%a)
    if b<=c:
        print('%.2f'%b)
        print('%.2f'%c)
    else:
        print('%.2f'%c)
        print('%.2f'%b)