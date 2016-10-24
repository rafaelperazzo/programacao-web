# -*- coding: utf-8 -*-
from __future__ import division

a=int(input('Digite o primeiro valor: '))
b=int(input('Digite o segundo valor: '))
c=int(input('Digite o terceiro valor: '))
d=int(input('Digite o quarto valor: '))

if a>10 or b>10 or c>10 or d>10 :
    print ('insira valores de 0 a 9')
else :
    if a==c or b==d :
        print ('V')
    elif a==d :
        print ('F')
    else :
        print ('N')
