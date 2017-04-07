# -*- coding: utf-8 -*-
a=float(input('Digite um número:'))
b=float(input('Digite um número:'))
c=float(input('Digite um número:'))
d=float(input('Digite um número:'))
if a>=b and a>=c and a>=d:
    if b<=c and b<=d:
        print('%d'%a)
        print('%d'%b)
    if c<=b and c<=d:
        print('%d'%a)
        print('%d'%c)
    if d<=b and d<=c:
        print('%d'%a)
        print('%d'%d)
        
        
        