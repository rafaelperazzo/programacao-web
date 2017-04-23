# -*- coding: utf-8 -*-
import math
n = int(input('Digite o valor de n: '))
soma=0
num=1
den=n
x=0
if n<0:
    n = (-1*n)
    
for num in range(1,n+1,1):
    soma=soma+(num/den)
    num=num+1
    x=x+1
    den=n-x
    
print(soma)    
    
    

