# -*- coding: utf-8 -*-
from __future__ import division
#ENTRADA
a=int(input('digite o valor de a:'))
b=int(input('digite o valor de b:'))
c=int(input('digite o valor de c:'))
if a<0:
    a=a*(-1)
if b<0:
    b=b*(-1)
if c<0:
    c=c*(-1)
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

