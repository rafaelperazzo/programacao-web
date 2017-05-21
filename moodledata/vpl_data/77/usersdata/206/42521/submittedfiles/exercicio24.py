# -*- coding: utf-8 -*-
import math

a=int(input('Digite a:')) 
b=int(input('Digite b:'))

for i in range (1,a+1,1):
    if (a%i==0) and (b%i==0): 
        MDC=i
print(MDC)