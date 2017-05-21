# -*- coding: utf-8 -*-
import math
n=int(input('Digite a quantidade de múltiplos:'))
a=int(input('Digite um número:'))
b=int(input('Digite um número:'))
i=2

while (n>0):
    if i%a==0 or i%b==0:
        print(i)
        i=i+1
        n=n-1
        
  
