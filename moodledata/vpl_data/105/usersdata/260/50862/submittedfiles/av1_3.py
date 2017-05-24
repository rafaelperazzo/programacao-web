# -*- coding: utf-8 -*-
import math
j=50
i=50
k=50
primeiro_numero=int(input("digite o primeiro valor:"))
segundo_numero=int(input("digite o segundo valor:"))
terceiro_numero=int(input("digite o terceiro valor:"))

while primeiro_numero!=1:
    if primeiro_numero%i==0:
        primeiro_numero=primeiro_numero/i
        parcial_1= primeiro_numero*i
i=i-1
while segundo_numero!=1:
    if segundo_numero%j==0: 
        parcial_2=segundo_numero*j
        segundo_numero=segundo_numero/j
j=j-1
while terceiro_numero!=1:
    if terceiro_numero%k==0:    
        parcial_3=terceiro_numero*k
        terceiro_numero=terceiro_numero/k
k=k-1
total=parcial_1+parcial_2+parcial_3
print(total)

    
            
        
            
            
    
