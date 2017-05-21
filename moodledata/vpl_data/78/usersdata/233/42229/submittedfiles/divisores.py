# -*- coding: utf-8 -*-
import math
n=int(input('Digite a quantidade de divisrorer que será mostrada: '))
a=int(input('Digite um número qualquer: '))
b=int(input('Digite um número qualquer: '))
cont=1
termo=1
i=1
for termo in range(1,n+1,1):
    if i%a==0 or i%b==0:
        print=(i)
    i=i+1    
       