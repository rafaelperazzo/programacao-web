# -*- coding: utf-8 -*-
import math
n=int(input('digite n :'))
soma=0
for num in range (1,n+1,1):
    denominador=num**2
    if num%2==1:
        soma=soma+num/denominador
    else:
        soma=soma-num/denominador
    print('%.5f'%soma)    
