# -*- coding: utf-8 -*-
import math
a=int(input('digite um valor para a:'))
b=int(input('digite um valor para b:'))
termo=1
i=1
while i<=termo:
    if a>b:
        for termo in range (1,a+1,1):
            if (a%i)==0 and (b%i)==0:
                print(i)
            i=i+1
    else:
        for termo in range (1,a+1,1):
            if (a%i)==0 and (b%i)==0:
                print(i)
            i=i+1    
