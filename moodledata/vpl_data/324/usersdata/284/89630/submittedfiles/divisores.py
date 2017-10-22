# -*- coding: utf-8 -*-
import math

n=int(input('digite a quantidade: '))
a=int(input('digite o valor: '))
b=int(input('digite o valor: '))
numeroteste=1
contador=0
while(contador<n):
    if(numeroteste%a==0) or (numeroteste%b==0):
        print(numeroteste)
        numeroteste=numeroteste+1
        contador=contador+1
    else:
        numeroteste+1
  
        

        
    
    