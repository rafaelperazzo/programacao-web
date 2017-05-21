# -*- coding: utf-8 -*-
import math
a=int(input('digite a:'))
b=int(input('digite b:'))
n=int(input('digite n:'))
cont=0
for i in range(1,n+2,1):
    cont=cont+i
    if cont%a==0:
        print(cont)
    if cont%b==0:
        print(cont)
        
        
    
        