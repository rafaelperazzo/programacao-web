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
C = Cv*3 + Ce*1
F = Fv*3 + Fe*1

#3
if C>F:
    print('C')
if F>C:
    print('F')
if C==F and Cs>Fs:
    print('C')
if C==F and Fs>Cs:
    print('F')
if C==F and Cs==Fs:
    print('=')
    
    
    
   
