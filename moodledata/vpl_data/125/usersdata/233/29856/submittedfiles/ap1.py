# -*- coding: utf-8 -*-
a=float(input('Digite um número qualquer'))
b=float(input('Digite um número qualquer'))
c=float(input('Digite um número qualquer '))
if a<=b and a<=c:
    if b<=c:
        print('%f'%a)
        print('%f'%b)
        print('%f'%c)
    if c<=b:
        print('%f'%a)
        print('%f'%c)
        print('%f'%b)
elif b<=a and b<=c:
    if a<=c:
        print('%f'%b)
        print('%f'%a)
        print('%f'%c)
    if c<=a:
        print('%f'%b)
        print('%f'%c)
        print('%f'%a)
elif c<=a and c<=b:
    if a<=b:
        print('%f'%c)
        print('%f'%a)
        print('%f'%b)
    if b<=a:
        print('%f'%c)
        print('%f'%b)
        print('%f'%a)
    