# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO
#ENTRADA
n=input('insira um numero:')
soma=0
a=1
b=0
#PROCESSAMENTO
while i<=n:
    if(i%2==0):
        soma=soma-1/(a*(3**b))
    else:
        soma=soma+1/(a*(3**b))
    b=b+1
    a=a+2
soma=soma*(12**0.5)    
print('O valor de PI é %.6f' %soma)
