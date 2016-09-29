# -*- coding: utf-8 -*-
from __future__ import division
import math

Cv=input('Número de vitórias: ')
Ce=input('Número de empates: ')
Cs=input('Saldo de gols: ')
Fv=input('Número de vitórias: ')
Fe=input('Número de empates: ')
Fs=input('Saldo de gols: ')

if (3*Cv)+Ce>(3*Fv)+Fe:
    print ('C')
if (3*Cv)+Ce<(3*Fv)+Fe:
    print ('F')
if (3*Cv)+Ce==(3*Fv)+Fe and Cs>Fs:
    print ('C')
if (3*Cv)+Ce==(3*Fv)+Fe and Cs<Fs:
    print ('F')
if (3*Cv)+Ce+Cs==(3*Fv)+Fe+Fs:
    print ('=')