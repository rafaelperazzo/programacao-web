# -*- coding: utf-8 -*-
import math

n=int(input('Digite a quantidade de multiplos: '))
a=int(input('Digite o numero a : '))
b=int(input('DIgite o numero b : '))
numeroteste=0
contador=0
while(contador<=n):
    if (numeroteste%a)==0 or (numeroteste%b)==0:
        print(numeroteste)
        numeroteste=numeroteste +1
        contador= contador +1
    else:
       numeroteste= numeroteste +1
       contador=contador+1
  
  
  
  

        

