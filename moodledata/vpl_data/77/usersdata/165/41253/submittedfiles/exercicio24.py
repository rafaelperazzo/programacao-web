# -*- coding: utf-8 -*-
import math
a=int(input('digite um valor para a:'))
b=int(input('digite um valor para b:'))
c=0
mdc=0
if a<b:
    b=a
    c=b
    a=c
    
    for i in range (1,a+1,1):
        if a%i==0 and b%i==0:
            mdc=i
            
    print(mdc)  

else:
    for i in range (1,a+1,1):
        if a%i==0 and b%i==0:
            mdc=i
            
    print(mdc)
    

                
