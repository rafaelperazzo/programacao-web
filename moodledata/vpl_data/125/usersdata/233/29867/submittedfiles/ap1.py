# -*- coding: utf-8 -*-
a=float(input('Digite um número:'))
b=float(input('Digite um número:'))
c=float(input('Digite um número:'))
if a<=b and a<=c:
    if b<=c:
        print('%.2f'%a)
        print('%.2f'%b)
        print('%.2f'%c)
    if c<=b:
        print('%.2f'%a)
        print('%.2f'%c)
        print('%.2f'%b)
elif b<=a and b<=c:
    if a<=c:
        print('%2f'%b)
        print('%.2f'%a)
        print('%.2f'%c)
    if c<=a:
        print('%.2f'%b)
        print('%.2f'%c)
        print('%.2f'%a)
elif c<=a and c<=b:
    if a<=b:
        print('%.2f'%c)
        print('%.2f'%a)
        print('%.2f'%b)
    if b<=a:
        print('%.2f'%c)
        print('%.2f'%b)
        print('%.2f'%a)
    