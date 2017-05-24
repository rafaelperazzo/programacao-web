# -*- coding: utf-8 -*-
import math
j=9
primeiro_numero=int(input("digite o primeiro valor:"))
segundo_numero=int(input("digite o segundo valor:"))
terceiro_numero=int(input("digite o terceiro valor:"))
for i in range(1,10,1):
    if primeiro_numero % i== 0:
        parcial_1=primeiro_numero/i
        while parcial_1 !=1:
            if primeiro_numero % j == 0:
                parcial_1=primeiro_numero/j
                j=j-1
    p1=parcial_1
    if segundo_numero % i== 0:
        parcial_2=segundo_numero/i
        while parcial_2 !=1:
            if segundo_numero % j == 0:
                parcial_2=segundo_numero/j
                j=j-1
        p2=parcial_2
    if terceiro_numero % i== 0:
        parcial_3=terceiro_numero/i
        while parcial_3 !=1:
            if terceiro_numero % j == 0:
                parcial_3=terceiro_numero/j
                j=j-1
    p3=parcial_3
total=p1*p2*p3
print(total)
-----------
i=99
while primeiro_numero==1:
    if primeiro_numero%i==0
    parcial_1=primeiro_numero*i
    i=i-1
    
            
        
            
            
    
