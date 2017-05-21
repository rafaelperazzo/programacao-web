# -*- coding: utf-8 -*-
import math

n= int(input('Digite o número de termos desejados:'))

soma=0
DEN=1
i=1

while i<=n:
    if i%2==0:
        soma=-1/DEN
    else: 
        soma=1/DEN
    
    DEN=DEN+1
    i=i+1
print ('%d.5'%soma)
    
    

    


