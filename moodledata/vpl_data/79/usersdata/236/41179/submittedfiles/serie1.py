# -*- coding: utf-8 -*-
import math

n= int(input('Digite o número de termos desejados:'))

soma=0
DEN=1
for i in range (1,n+1,1):
    if i%2==0:
        soma=soma-(1/DEN)
        
    else:
        soma=soma+(1/DEN)
    DEN=DEN+1
print ('%.5d'%soma)

    


