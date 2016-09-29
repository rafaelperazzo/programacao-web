# -*- coding: utf-8 -*-
from __future__ import division
import math

cv = input('digite o número de vitórias do cormengo')
ce = input('digite o número de empates do cormengo')
cs = input('digite o saldo de gols do cormengo')
fv = input('digite o número de vitórias do flaminthians')
fe = input('digite o número de empates do flaminthians')
fs = input('digite o saldo de gols do flaminthians')

pv1 = 3*cv
pv2 = 3*fv
pe1 = 1*ce
pe2 = 1*fe

if (pv1+pe1)>(pv2+pe2):
    print('C')
elif (pv1+pe1)<(pv2+pe2):
    print('F')
elif (pv1+pe1)=(pv2+pe2):
    if cs>fs:
        print('C')
    elif fs>cs:
        print('F')
    elif cv=fv:
        print('=')
        
        if 
        

    
