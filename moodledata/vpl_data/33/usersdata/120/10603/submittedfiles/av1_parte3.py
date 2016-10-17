# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO
#ENTRADA
n=input('insira um numero:')
soma=0
j=1
i=0
#PROCESSAMENTO
while i<=n:
    if(i%2==0):
        soma=soma-1/(j*(3**i))
    else:
        soma=soma+1/(j*(3**i))
    i=i+1
    j=j+2
soma=soma*(12**0.5)    
print('O valor de PI é %.6f' %soma)
