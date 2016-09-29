# -*- coding: utf-8 -*-
from __future__ import division
import math

Cv=('Número de vitórias: ')
Ce=('Número de empates: ')
Cs=('Saldo de gols: ')
Fv=('Número de vitórias: ')
Fe=('Número de empates: ')
Fs=('Saldo de gols: ')

if (3*Cv)+Ce>(3*Fv)+Fe:
    print ('C')
else:
    print ('F')
if (3*Cv)+Ce==(3*Fv)+Fe and Cs>Fs:
    print ('C')
if (3*Cv)+Ce==(3*Fv)+Fe and Cs<Fs:
    print ('F')
if (3*Cv)+Ce+Cs==(3*Fv)+Fe+Fs:
    print ('=')