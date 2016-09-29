# -*- coding: utf-8 -*-
from __future__ import division
import math

#Entrada

f= input ('Digite o valor de f:') 
L= input ('Digite o valor de L:') 
Q= input ('Digite o valor de Q:')
DeltaH= input ('Digite o valor de DeltaH:') 
v= input ('Digite o valor de v:') 

#Processamento 

D=((8*f*L*(Q**2))/((math.pi**2)*9,81*DeltaH))**(1/5)
Rey=(4*Q)/(math.pi*D*v) 
k=0,25/((math.log10((0,000002/(3,7*D))+(5,74/(Rey**0,9)))**2

#Saida

print('Os valores de D, Rey e k são:%.4f,%.4f e %.4f'%(D,Rey,k))
