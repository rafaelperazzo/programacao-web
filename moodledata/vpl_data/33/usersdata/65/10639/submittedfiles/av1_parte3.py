# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO

n=input('Digite n:')

i=0
denominador=1
soma=0

while (i<=n):
    
    if i%2!=0:
        soma=soma+(1/(denominador*(3**i)))
    
    else:
        soma=soma-(1/(denominador*(3**i)))
        
soma=soma*(12**(1/2))

print(soma)
        