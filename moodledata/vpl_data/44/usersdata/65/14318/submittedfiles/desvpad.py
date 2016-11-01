# -*- coding: utf-8 -*-
from __future__ import division
import math

#comece abaixo

n=input('Digite n: ')

l=[]

#LISTA
for i in range(0,n,1):
    l.append(input('Digite um elemento: '))
 
#PRIMEIROeULTIMO   
print('%.2f' %l[0])
print('%.2f' %(l[len(l)-1]))

#MEDIA
soma=0

for i in range(0,n,1):
    soma=(soma+l[i])
    
media=((soma)/(len(l)))
print('%.2f' %media)

#DESVIO
d=0

for i in range(0,n,1):
    d=d+(((1/(n-1))*((l[i]-media)**2))**(1/2))
    
    
print('%.2f'%d)  
