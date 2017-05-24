# -*- coding: utf-8 -*-
import math
i=10
j=10
k=10
primeiro_numero=int(input("digite o primeiro valor:"))
segundo_numero=int(input("digite o segundo valor:"))
terceiro_numero=int(input("digite o terceiro valor:"))
parcial_1=1
parcial_2=1
parcial_3=1
while primeiro_numero!=1:
    if primeiro_numero%i==0:
        primeiro_numero=primeiro_numero/i
        parcial_1=parcial_1*i
    i=i-1
while segundo_numero!=1:
    if segundo_numero%j==0: 
        segundo_numero=segundo_numero/j
        parcial_2=parcial_2*j
    j=j-1
while  terceiro_numero!=1:
    if terceiro_numero%k==0:    
        terceiro_numero=terceiro_numero/k
        parcial_3=parcial_3*k
    k=k-1
total=parcial_1+parcial_2+parcial_3
print(total)

    
            
        
            
            
    
