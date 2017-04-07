# -*- coding: utf-8 -*-
a=float(input('Digite um número:'))
b=float(input('Digite um número:'))
c=float(input('Digite um número:'))
if a<=b and a<=c:
    if b<=c:
        print('%.1f'%a)
        print('%.1f'%b)
        print('%.1f'%c)
    if c<=b:
        print('%.1f'%a)
        print('%.1f'%c)
        print('%.1f'%b)
elif b<=a and b<=c:
    if a<=c:
        print('%1f'%b)
        print('%.1f'%a)
        print('%.1f'%c)
    if c<=a:
        print('%.1f'%b)
        print('%.1f'%c)
        print('%.1f'%a)
elif c<=a and c<=b:
    if a<=b:
        print('%.1f'%c)
        print('%.1f'%a)
        print('%.1f'%b)
    if b<=a:
        print('%.1f'%c)
        print('%.1f'%b)
        print('%.1f'%a)
    