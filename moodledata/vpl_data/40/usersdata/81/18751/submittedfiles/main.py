# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

m=int(input('Digite m:'))
e=input('Digite o epsilon para o cosseno:')

soma_pi=0
j=2
for i in range (0,m,1):
    if i%2==0:
        soma_pi=soma_pi+(4/(j*(j+1)*(j+2)))
    else:
        soma_pi=soma_pi-(4/(j*(j+1)*(j+2)))
    j=j+2    
pi=3+soma_pi


soma_cosseno=0
j=2

while i<m and soma_cosseno==e:
    if i%2!=0:
        soma_cosseno=soma_cosseno+(((pi/5)**j)/fatorial(j))
    else:
        soma_cosseno=soma_cosseno-(((pi/5)**j)/fatorial(j))
    j=j+2
    i=i+1
    
cosseno=1-soma_cosseno


razaoAurea= 2*cosseno
print('%.15f' %pi)
print('%.15f' %razaoAurea)