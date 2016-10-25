# -*- coding: utf-8 -*-
from __future__ import division
#Entrada
a=int(input('insira o valor de a:'))
b=int(input('insira o valor de b:'))
c=int(input('insira o valor de c:'))



#Processamento
if a<b and ((c%a)%b)==0 
    
    q1=c//a
    q2=(c%a)//b
    print(q1)
    print(q2)
    
if b<a and ((c%b)%a)==0
    q1=c//b
    q2=(c%b)//a
    print(q1)
    print(q2)
else:
    print('N')
    