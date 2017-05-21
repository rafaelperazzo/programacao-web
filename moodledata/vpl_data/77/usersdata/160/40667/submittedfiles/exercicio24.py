# -*- coding: utf-8 -*-
import math

a=int(input('Digite a:'))
b=int(input('Digite b:'))

cont=0
for i in range(a,b+1,1):
    if a%i==0 and b%i==0:
        cont=cont+1
        print(cont)
        
        
    
    
    

    
    
