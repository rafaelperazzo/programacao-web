# -*- coding: utf-8 -*-
import math

a=int(input('Digite a:'))
b=int(input('Digite b:'))


i=1
if a>b:
    maior=a
    
else:
    maior=b
    
for i in range(1,maior):
    a%i==0 and b%i==0:
        mdc=i+1
        
print(mdc)
    
    
    

    
    
