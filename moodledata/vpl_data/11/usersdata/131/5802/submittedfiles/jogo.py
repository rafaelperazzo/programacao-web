# -*- coding: utf-8 -*-
from __future__ import division
import math

#Entrada

Cv = float(input('Numero de vitorias para o C: '))
Ce = float(input('Numero de empates para o C: '))
Cs = float(input('Saldo de gols para o C: '))
Fv = float(input('Numero de vitorias para o F: '))
Fe = float(input('Numero de empates para o F: '))
Fs = float(input('Saldo de gols para o F: '))

#Processamento e Saída

if Cv > Fv:
    print('C')

if (Cv == Fv) and (Ce > Fe):
    print('C')

if (Cv == Fv) and (Ce == Fe) and (Cs > Fs):
    print('C')
    
if Fv > Cv:
    print ('F')
    
if (Fv == Cv) and (Fe > Ce):
    print('F')
    
if (Fv == Cv) and (Fe == Ce) and (Fs > Cs):
    print('F')
    
if (Fv == Cv) and (Fe == Ce) and (Fs == Cs):
    print('=')
    
