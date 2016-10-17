# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO
#ENTRADA
n=input('insira um numero:')
soma=0
i=1
j=0
#PROCESSAMENTO
while i<=n:
    if(i%2==0):
        soma=soma-1/(a*(3**j))
    else:
        soma=soma+1/(a*(3**j))
    j=j+1
    a=a+2
    i=i+1
soma=soma*(12**0.5)    
print('O valor de PI é %.6f' %soma)
