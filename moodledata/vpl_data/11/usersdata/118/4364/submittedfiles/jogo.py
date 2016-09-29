# -*- coding: utf-8 -*-
from __future__ import division
import math

#1
Cv = input('Digite o número de vitórias do Cormengo :')
Ce = input('Digite o número de empates do Cormengo :')
Cs = input('Digite o número de saldo de gols do Cormengo :')
Fv = input('Digite o número de vitórias do Flaminthias :')
Fe = input('Digite o número de empates do Flaminthias :')
Fs = input('Digite o número de saldo de gols do Flaminthias :')

#2
if Cv>Fv and Ce>Fe:
    print('C')
if Fv>Cv and Fe>Ce
    print('F')
if Cv==Fv and Ce==Fe and Cs>Fs:
    print('C')
if Cv==Fv and Ce==Fe and Fs>Cs:
    print('F')
if Cv==Fv and Ce==Fe and Cs==Fs:
    print('=')
    
