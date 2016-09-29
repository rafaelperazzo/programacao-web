# -*- coding: utf-8 -*-
from __future__ import division
import math
Cv=input('Número de vitórias do Cormengo:')
Ce=input('Número de empartes do Cormengo:')
Cs=input('Saldo de gols do Cormengo:')
Fv=input('Número do vitórias do Flaminthians:')
Fe=input('Número de empates do Flaminthians:')
Fs=input('Saldo de gols do Flaminthians:')
NVC=Cv*3
NEC=Ce*1
NVF=Fv*3
NEF=Fe*1
if (NVC+NEC)>(NVF+NEF):
    print('C')
if (NVF+NEF)>(NVC+NEC):
    print('F')
if (NVC+NEC)==(NVF+NEF) and Fs>Cs:
    print('F')
if (NVC+NEC)==(NVF+NEF) and Cs>Fs:
    print('C')
if (NVC+NEC)==(NVF+NEF) and Cs==Fs:
    print('=')

    