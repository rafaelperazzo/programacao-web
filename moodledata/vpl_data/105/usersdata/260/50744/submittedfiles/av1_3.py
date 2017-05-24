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
print(parcial_1)
                
        
            
            
    
