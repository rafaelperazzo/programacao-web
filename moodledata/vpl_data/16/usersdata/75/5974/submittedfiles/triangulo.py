# -*- coding: utf-8 -*-
from __future__ import division
import math

#Entrada

a= int(input ('Digite o valor do lado a:'))
b= int(input ('Digite o valor do lado b:'))
c= int(input ('Digite o valor do lado c:'))

#Processamento e Saida

if (a<b+c):
    print ('S')
    if (a**2==((b**2)+(c**2))):
        print ('Re')
    elif (a>(b**2)+(c**2)):
        print ('Ob')
    else: 
        print ('Ac')
    
    if (a==b==c):
        print ('Eq')
    elif (b==c!=a):
        print ('Is')
    else:
        print ('Es')

else: 
    print ('N')
    