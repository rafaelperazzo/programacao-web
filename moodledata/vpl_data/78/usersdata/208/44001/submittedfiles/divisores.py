# -*- coding: utf-8 -*-
import math
n=int(input('escreva n:'))
a=int(imput('escreva a:'))
b=int(imput('escreva b:'))
for i in range(1,n+4,1):
    if i%a==0 and i%b==0:
        print(i)
    elif i%a==0:
            print(i)
    elif i%b==0:
                print(i)
