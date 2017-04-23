# -*- coding: utf-8 -*-
from __future__ import division
import math

saque=int(input('digite o valor:'))
if saque>=20:
    v1=saque/20
    print('notas de 20 :%.d'%v1)
if saque>=10:
    v2=(saque%20)/10
    print('notas de 10 :%.d'%v2)
if saque>=5:
    v3=(saque%10)/5
    print('notas de 5 :%.d'%v3)
if saque>=2:
    v4=(saque%5)/2
    print('notas de 2 :%.d'%v4)
if saque<>1:
    v5=(saque%2)/1
    print('notas de 1 :%.d'%v5)
    
       

   
    
