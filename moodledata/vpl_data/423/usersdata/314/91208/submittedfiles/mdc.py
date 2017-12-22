# -*- coding: utf-8 -*-
import math

n1=int(input('Digite um numero inteiro positivo: '))
n2=int(input('Digite um numero inteiro positivo: '))

 
if n1<n2:
    menor=n1
else:
    menor=n2
while n1%menor!=0 or n2%menor!=0:
        menor=menor-1
print(menor)     
        
 
    

