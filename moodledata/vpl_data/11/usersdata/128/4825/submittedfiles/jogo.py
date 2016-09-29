# -*- coding: utf-8 -*-
from __future__ import division
import math

cv=input('Número de vitórias do Cormengo: ')
ce=input('Número de empates do Cormengo: ')
cs=input('Saldo de gols do Cormengo: ')

fv=input('Número de vitórias do Flaminthians: ')
fe=input('Número de empates do Flaminthians: ')
fs=input('Saldo de gols do Flaminthians: ')

pontosC= (cv*3)+ce
pontosF= (fv*3)+fe

if pontosC > pontosF:
    print ('C')

elif pontosF > pontosC:
    print ('F')

else:
    if cs>fs:
        print ('C')
    elif fs>cs:
        print ('F')
    else:
        print ('=')