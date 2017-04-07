# -*- coding: utf-8 -*-
a=float(input('digite a:'))
b=float(input('digite b:'))
c=float(input('digite c:'))
if a>b and b>c and a>c:
    print('%0.f' %c)
    print('%0.f' %b)
    print('%0.f' %a)
if a>b and c>b and a>c:
    print('%0.f' %b)
    print('%0.f' %c)
    print('%0.f' %a)
if a>b and c>a and c>b:
    print('%0.f' %b)
    print('%0.f' %a)
    print('%0.f' %c)
if b>a and c>a and c>b:
    print('%0.f' %a)
    print('%0.f' %b)
    print('%0.f' %c)
if b>a and a>c and b>c:
    print('%0.f' %c)
    print('%0.f' %a)
    print('%0.f' %b)
if b>a and c>a and b>c:
    print('%.0f' %a)
    print('%.0f' %c)
    print('%.0f' %b)
if b==a or a==c or b==c:
    print('numeros iguais')
    
