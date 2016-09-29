# -*- coding: utf-8 -*-
from __future__ import division
import math

Cv=('Digite o número de vitórias do Cormengo: ')
Ce=('Digite o número de empates do Cormengo: ')
Cg=('Digite o saldo de gols do Cormengo: ')

Fv=('Digite o número de vitórias do Flaminthias: ')
Fe=('Digite o número de empates do Flaminthias: ')
Fg=('Digite o saldo de gols do Flaminthias: ')

VCormengo=(Cv*3+Ce*1)
VFlaminthias=(Fv*3+Fe*1)

if (VCormengo>VFlaminthias):
    print('C')
    
if (VCormengo<VFlaminthias):
    print('F')
    
if (VCormengo==VFlaminthias):
    print('=')