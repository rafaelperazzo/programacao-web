# -*- coding: utf-8 -*-
import math
n= int(input('Digite o número de divisores desejados:'))
a= int(input('Digite o Primeiro número:'))
b= int(input('Digite o Segundo número:'))

if b<a:
    x=a
    a=b
    b=x
    
i=0
while i<=n:
    a=a*i
    b=b*i
    print(a)
    print(b)
    i=i+1
    
    
    
  



