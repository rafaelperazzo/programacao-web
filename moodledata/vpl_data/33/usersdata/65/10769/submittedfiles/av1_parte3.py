# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO

n=input('Digite n:')

i=1
denominador=1
soma=0

while (i<=n):
    
    if i%2!=0:
        soma=soma+(1/(denominador*(3**(i-1))))
    
    else:
        soma=soma-(1/(denominador*(3**(i-1))))
    
      
    i=i+1
    denominador=denominador+2
    
        
soma=soma*(12**(1/2))

print('%.6f'%soma)
        