# -*- coding: utf-8 -*-
a=float(input('Digite um número:'))
b=float(input('Digite um número:'))
c=float(input('Digite um número:'))
if a<=b and a<=c:
    if b<=c:
        print('%.d'%a)
        print('%.d'%b)
        print('%.d'%c)
    if c<=b:
        print('%.d'%a)
        print('%.d'%c)
        print('%.d'%b)
elif b<=a and b<=c:
    if a<=c:
        print('%.d'%b)
        print('%.d'%a)
        print('%.d'%c)
    if c<=a:
        print('%.d'%b)
        print('%.d'%c)
        print('%.d'%a)
elif c<=a and c<=b:
    if a<=b:
        print('%.d'%c)
        print('%.d'%a)
        print('%.d'%b)
    if b<=a:
        print('%.d'%c)
        print('%.d'%b)
        print('%.d'%a)
    