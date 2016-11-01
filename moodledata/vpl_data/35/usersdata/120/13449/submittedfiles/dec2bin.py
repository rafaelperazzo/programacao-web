# -*- coding: utf-8 -*-
from  __future__  import division
p=int(input('insira o valor de p:'))
q=int(input('insira o valor de q:'))
#Processamento
contp=contq=cont=0
x=p
while x>0:
    x=x//10
    contp+=1
np=contp
t=q
while t>0:
    t=t//10
    contq+=1
nq=contq
if np<=nq:
    a=10**np
    while q>0:
        if q%a==p:
            cont+=1
            break
        q=q//10
if  cont>0:
    print ('S')
else:
    print('N')