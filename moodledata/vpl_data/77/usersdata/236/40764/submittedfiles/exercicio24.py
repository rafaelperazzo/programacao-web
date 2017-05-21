# -*- coding: utf-8 -*-
import math
a= int(input('Digite o Primeiro número:'))
b= int(input('Digite o Segundo número:'))

#MAIOR SEMPRE SERÁ "a"
if a<b:
    x=a
    a=b
    b=x

i=1

while i<=b:
    if b%i==0 and a%i==0:
        DC=i
    i=i+1
print (DC)
        
        
      
   
    







