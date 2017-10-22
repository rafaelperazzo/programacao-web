# -*- coding: utf-8 -*-
import math

a=int(input('Digite a: '))
b=int(input('Digite b: '))
c=int(input('Digite c: '))

i=1
if ((a>b) and (a>c)):
    while (i<=(a*b*c)):
        if (i%a==0) and (i%b==0) and (i%c==0):
            print(i)
            break
        else:
            i=i+1

    