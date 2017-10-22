# -*- coding: utf-8 -*-
import math

#COMECE SEU CÓDIGO ABAIXO DESTA LINHA
a=int(input('Carta 1:')) 
b=int(input('Carta 2:')) 
c=int(input('Carta 3:')) 
d=int(input('Carta 4:')) 
e=int(input('Carta 5:')) 

if (a<b) and (b<c) and (c<d) and (d<e):
    print ('C')
elif (a>b) and (b>c) and (c>d) and (d>e):
    print ('D')
else:
    print ('N')


