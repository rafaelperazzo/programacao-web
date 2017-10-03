# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
a= float(input('Digite um número: '))
b= float(input('Digite outro número: '))
c= float(input('Digite outro número: '))
d= float(input('Digite outro número: '))

if a > b and a > c and a > d :
    if b < a and b < c and b < d :
        print ('Maior=%.f, menor=%.f' % (a, b))
else :
    print ('Maior=%.f, menor=%.f' % (b, a))
    