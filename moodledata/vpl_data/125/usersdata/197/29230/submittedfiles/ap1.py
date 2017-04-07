# -*- coding: utf-8 -*-
a=float(input('Digite o valor de a:'))
b=float(input('Digite o valor de b:'))
c=float(input('Digite o valor de c:'))
if c<=a and c<=b:
    print('%f'%c)
    if b<=a:
        print('%f'%b)
        print('%f'%a)
    else:
        print('%f'%a)
        print('%f'%b)
elif b<=a and b<=c:
    print('%f'%b)
    if a<=c:
        print('%f'%a)
        print('%f'%c)
    else:
        print('%f'%c)
        print('%f'%a)
else:
    print('%f'%a)
    if b<=c:
        print('%f'%b)
        print('%f'%c)
    else:
        print('%f'%c)
        print('%f'%b)
    