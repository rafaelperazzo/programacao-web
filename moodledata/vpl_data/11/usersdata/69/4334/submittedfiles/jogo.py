# -*- coding: utf-8 -*-
from __future__ import division
import math
Cv=input('Digite o número de vitórias do Cormengo:')
Ce=input('Digite o número de empates do Cormengo:')
Cs=input('DIgite o saldo de gols do Cormengo:')
Fv=input('Digite o número de vitórias do Flaminthians:')
Fe=input('Digite o número de empates do Flaminthians:')
Fs=input('DIgite o saldo de gols do Flaminthians:')
Pc=((Cv*3)+Ce)
Pf=((Fv*3)+Fe)
if Pc>Pf:
    print('C')
if Pf>Pc:
    print('F')
if Cs>Fs:
    print('C')
if Fs>Cs:
    print('F')
else:
    print('=')