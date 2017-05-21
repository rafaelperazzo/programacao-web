# -*- coding: utf-8 -*-
import math
n=int(input('digite o valor de n:'))
a=int(input('digite o valor de a:'))
b=int(input('digite o valor de b:'))
cont=0
i=1

while cont<n:
    if i%a==0 or i%b==0:
        print(i)
        cont=cont+1
    i+i=1    
