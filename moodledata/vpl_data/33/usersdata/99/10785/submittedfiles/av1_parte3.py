# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO
n=input('Digite o valor de n:')

j=1
i=0
cont=0

while i<=n:
    if i%2==0:
        cont=cont+(12**0.5)*(1/(j*(3**i)))
        
    else:
        cont=cont+(12**0.5)*(-1/(j*(3**i)))
        
    j=j+2
    i=i+1
    
print ('%.6f'%cont)