# -*- coding: utf-8 -*-
from __future__ import division

a=int(input('digite o velor de a:'))
b=int(input('digite o velor de b:'))
c=int(input('digite o velor de c:'))
na=0
nb=0
cont=0

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