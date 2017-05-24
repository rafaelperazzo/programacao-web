# -*- coding: utf-8 -*-
import math
i=10
primeiro_numero=int(input("digite o primeiro valor:"))
segundo_numero=int(input("digite o segundo valor:"))
terceiro_numero=int(input("digite o terceiro valor:"))

while primeiro_numero!=1 and segundo_numero!=1 and terceiro_numero!=1 :
    if primeiro_numero%i==0:
        primeiro_numero=primeiro_numero/i
        parcial_1=parcial_1*i
    i=i-1
    if segundo_numero%i==0: 
        parcial_2=parcial_2*i
        segundo_numero=segundo_numero/i
    i=i-1
    if terceiro_numero%i==0:    
        parcial_3=parcial_3_numero*i
        terceiro_numero=terceiro_numero/i
    i=i-1
    total=parcial_1+parcial_2+parcial_3
print(total)

    
            
        
            
            
    
