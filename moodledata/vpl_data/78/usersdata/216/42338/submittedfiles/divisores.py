# -*- coding: utf-8 -*-
import math
n=int(input('Digite a quantidade de múltiplos:'))
a=int(input('Digite um número:'))
b=int(input('Digite um número:'))
i=1
j=1
for i in range(1,j,1):
    if n>0:
        if (i%a==0) or (i%b==0):
            print(i)
            n=n-1
            j=j+1
        
        
        
        
