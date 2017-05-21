# -*- coding: utf-8 -*-
import math
n=float(input('digite o valor do multiplo:'))
n=int(n)
x=float(input('digite seu primeiro numero:'))
x=int(x)
y=float(input('digite seu segundo numero:'))
y=int(y)
if x<0 or y<0 or (x<0 and y<0) or :
    print('erro.este programa so admite numeros positivos')
else:
    ix=1
    iy=1
    mx=0
    my=0
    cont=0
    while cont<n:
        mx=ix*x
        my=iy*y
        if mx<my:
            print(mx)
            ix=ix+1
        elif my<mx:
            print(my)
            iy=iy+1
        else:
            print(my)
            ix=ix+1
            iy=iy+1
            cont+cont+1