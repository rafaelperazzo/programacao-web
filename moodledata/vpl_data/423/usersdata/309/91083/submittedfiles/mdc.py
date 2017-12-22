# -*- coding: utf-8 -*-
import math
num1= int(input("Digite um número inteiro positivo:"))
num2= int(input("Digite um número inteiro positivo:"))
i=0
if num1>num2:
   i=num2
else:
    i=num1
    
while i>0 :
    
    if num1%i==0 and num2%i==0 :
        mdc=i
        break 
    else:
        i=i-1

print (mdc)
    



