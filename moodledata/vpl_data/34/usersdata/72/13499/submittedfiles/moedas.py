# -*- coding: utf-8 -*-
from __future__ import division
#ENTRADA
a=int(input('digite o valor de a:'))
b=int(input('digite o valor de b:'))
c=int(input('digite o valor de c:'))
na=0
nb=0
cont=0
    
#SAIDA
while na<=c//a:
    nb=(c-na*a)//b
    if na*a+nb*b==c:
        cont=cont+1
        break
    else:
        na=na+1
    if cont>0:
        print (na)
        print (nb)
    else:
        print ('N')

