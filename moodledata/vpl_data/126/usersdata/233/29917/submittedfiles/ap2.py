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
elif b>=a and b>=c and b>=d:
    if a<=c and a<=d:
        print('%d'%b)
        print('%d'%a)
    if c<=a and c<=d:
        print('%d'%b)
        print('%d'%c)
    if d<=a and d<=c:
        print('%d'%b)
        print('%d'%d)
elif c>=a and c>=b and c>=d:
    if a<=b and a<=d:
        print('%d'%c)
        print('%d'%a)
    if b<=a and b<=d:
        print('%d'%c)
        print('%d'%b)
elif d>=a and d>=b and d>=c:
    if a<=b and a<=c:
        print('%d'%d)
        print('%d'%a)
    if b<=a and b<=c:
        print('%d'%d)
        print('%d'%b)
    if c<=a and c<=b:
        print('%d'%d)
        print('%d'%c)
    

        
        
        