# -*- coding: utf-8 -*-
from __future__ import division
import math

a= input('Digite o primeiro valor: ')
b= input('Digite o segundo valor: ')
c= input('Digite o terceiro valor: ')
d= input('Digite o quarto valor: ')

if a==b==c==d:
    print('N')
else:
    if a>b and ((c<=b) or (c<=d)) and (d<=c):
        print('S')
    else:
        if (b>a) and (b>c) and (d<=c):
            print('S')
        else:
            if c>b and c>d and (a<=b):
                print('S')
            else:
                if d>c and (b<=c or b<=a) and a<=b:
                    print('S')
                else:
                    print('N')