# -*- coding: utf-8 -*-
import math
n=int(input('digite o valor de multiplos n:'))
a=int(input('digite o valor de a:'))
b=int(input('digite o valor de b:'))
i=1
contador=0
while contador<=6:
    a1=a*i
    b1=b*i
    if a1<=b1:
        print(a1)
        if a1!=b1:
            print(b1)
            contador=contador+2
        else:
            contador=contador+1
    else:
        print(b1)
        if a1!=b1:
            print(a1)
            contador=contador+2
        else:
            contador=contador+1
    i=i+1    