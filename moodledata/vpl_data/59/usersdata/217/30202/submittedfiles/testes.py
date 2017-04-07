# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
a=float(input('digite um valor a:'))
b=float(input('digite um valor b:'))
c=float(input('digite um valor c:'))
if a!=b and a!=c and b!=c:
    print('diferentes')
elif a==b and b==c:
    print('iguais')
else:
        print('2 iguais')
