# -*- coding: utf-8 -*-
import math
a=int(input('Digite o valor de a: '))
b=int(input('Digite o valor de b: '))
if a>b:
    for i in range (2,b,1):
        if (a%i)==0 and (b%i)==0:
            print(i)
        else:
            print ('1')
if b>a:
    for i in range (2,a,1):
        if (b%i)==0 and (a%i)==0:
            print (i)
        else:
            print ('1')