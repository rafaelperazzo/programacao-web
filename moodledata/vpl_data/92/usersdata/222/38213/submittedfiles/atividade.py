# -*- coding: utf-8 -*-
import math
n=int(input('n:')
if  n<0:
    n=n*(-1)
    termo=1
    soma=0
    denominador=n
    while   termo<=n:
        soma=soma+termo/denominador
        denominador=denominador-1
        termo=termo+1
    print('%.5f' %soma)
else:
    termo=1
    soma=0
    denominador=n
    while   termo<=n:
        soma=soma+termo/denominador
        denominador=denominador-1
        termo=termo+1
    print('%.5f' %soma)
     
        
        
        

