# -*- coding: utf-8 -*-
import math

a=int(input('Digite a: '))
b=int(input('Digite b: '))
c=int(input('Digite c: '))

i=1
if ((a>b) and (a>c)):
    while (i<=a):
        if (i%a==0) and (i%b==0) and (i%c==0):
            print(i)
        else:
            i=i+1
elif ((b>a) and (b>c)):
    while (i<=b):
        if (i%a==0) and (i%b==0) and (i%c==0):
            print(i)
        else:
            i=i+1
elif ((c>a) and (c>b)):
    while (i<=c):
        if (i%a==0) and (i%b==0) and (i%c==0):
            print(i)
        else:
            i=i+1
            
    