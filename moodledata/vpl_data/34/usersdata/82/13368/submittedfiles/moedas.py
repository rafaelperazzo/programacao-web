# -*- coding: utf-8 -*-
from __future__ import division

a= int(input('Digite o valor de a:'))
b= int(input('Digite o valor de b:'))
c= int(input('Digite o valor de c:'))

qa= 0
qb= 0
contador=0

while qa<=(c//a):
    qb=(c-qa*a)//b
    if qa*a+qb*b==c:
        contador=contador+1
        break
    else:
        qa=qa+1
if contador>0:
    print (%qa)
    print (%qb)
else:
    print ('N')
    

        
        

      
    