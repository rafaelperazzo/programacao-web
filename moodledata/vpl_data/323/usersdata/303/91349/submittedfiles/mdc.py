# -*- coding: utf-8 -*-
import math
x=int(input('DIGITE O VALOR DE X:'))
y=int(input('DIGITE O VALOR DE Y:'))
i=1

while (i<=x):
    if (x%i)==0 and (y%i)==0:
        MDC=i
    
    i=i+1
print(MDC)
    
