# -*- coding: utf-8 -*-
from __future__ import division
import math

Cv=input('Digite o número de vitórias do Cormengo: ')
Ce=input('Digite o número de empates do Cormengo: ')
Cg=input('Digite o saldo de gols do Cormengo: ')

Fv=input('Digite o número de vitórias do Flaminthias: ')
Fe=input('Digite o número de empates do Flaminthias: ')
Fg=input('Digite o saldo de gols do Flaminthias: ')

VCormengo=(Cv*3+Ce*1)
VFlaminthias=(Fv*3+Fe*1)

if (VCormengo>VFlaminthias):
    print('C')
    
if (VCormengo<VFlaminthias):
    print('F')
    
if (VCormengo==VFlaminthias):
    print('=')