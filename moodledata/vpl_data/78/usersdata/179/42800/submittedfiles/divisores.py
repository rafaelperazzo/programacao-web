# -*- coding: utf-8 -*-
import math
a=int(input('digite a:'))
b=int(input('digite b:'))
n=int(input('digite n:'))
cont=1
for i in range(1,n+1,1):
    cont=cont+i
    if i%a==0:
        print(cont)
    if i%b==0:
        print(cont)
        
        
    
        