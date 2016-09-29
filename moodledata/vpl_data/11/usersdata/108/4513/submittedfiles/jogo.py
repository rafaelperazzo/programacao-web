# -*- coding: utf-8 -*-
from __future__ import division
import math

Cv = input ('Digite o número de vitórias do Cormengo:')
Ce = input ('Digite o número de empates do Cormengo:')
Cs = input ('Digite o saldo de gols do Cormengo:')
Fv = input ('Digite o número de vitórias do Flaminthians:')
Fe = input ('Digite o número de empates do Flaminthians:')
Fs = input ('Digite o saldo de gols do Flaminthians:')

if ((Cv*3+Ce)>(Fv*3+Fe)):
    print ('C')
elif ((Cv*3+Ce)<(Fv*3+Fe)):
    print ('F')
else: 
    print ('=')
