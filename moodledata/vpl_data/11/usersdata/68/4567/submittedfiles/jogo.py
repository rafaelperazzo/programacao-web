# -*- coding: utf-8 -*-
from __future__ import division
import math
#ENTRADA:
Cv= input ('Digite o número de vitórias do Cormengo:')
Ce= input ('Digite o número de empates do Cormengo:')
Cs= input ('Digite o saldo de gols do Cormengo:')

Fv= input ('Digite o número de vitórias do Flaminthians:')
Fe= input ('Digite o número de empates do Flaminthians:')
Fs= input ('Digite o número de gols do Flaminthians:')

if ((Cv*3)+Ce+Cs)>((Fv*3)+Fe+Fs):
    print ('C')
elif ((Fv*3)+Fe+Fs)>((Cv*3)+Ce+Cs):
    print ('F')
else:
    print ('=')