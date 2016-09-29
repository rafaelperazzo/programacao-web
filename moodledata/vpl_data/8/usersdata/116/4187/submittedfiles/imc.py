# -*- coding: utf-8 -*-
from __future__ import division

p = input ('insira o seu peso:')
h = input ('isira sua altura:') 

imc=p/(h**2)

if imc<20 :
    print ('BAIXO')
if imc>=20 and imc<=25: 
    print ('NORMAL') 
if imc>25 and imc<=30:
    print ('SOBREPESO') 
if imc>30 and imc<=40:
    print ('OBSIDADE') 
else:
    print ('OBSIDADE GRAVE') 