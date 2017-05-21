# -*- coding: utf-8 -*-
import math
a=int(input('digite um valor para a:'))
b=int(input('digite um valor para b:'))
if a>b:
    for i in range (2,a,1):
        if (a%i)==0 and (b%i)==0:
            print(i)
    
else:
    for i in range (2,b,1):
        if (a%i)==0 and (b%i)==0:
            print(i)
            i=i+1    
