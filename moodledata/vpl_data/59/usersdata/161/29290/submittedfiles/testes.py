# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
a=int(input('Digite a:'))
b=int(input('Digite b:'))
c=int(input('Digite c:'))
if a>b and a>c:
    print('%d'%a)
    if b>c:
        print('%d'%b)
        print('%d'%c)
    if c<b:
        print('%d'%c)
        print('%d'%b)
if b>a and b>c:
    print('%d'%b)
    if a>c:
        print('%d'%a)
        print('%d'%c)
    if c>a:
        print('%d'%c)
        print('%d'%a)
if c>a and c>b:
    print('%d'%c)
    if a>b:
        print('%d'%a)
        print('%d'%b)
    if b>a:
        print('%d'%b)
        print('%d'%a)

        