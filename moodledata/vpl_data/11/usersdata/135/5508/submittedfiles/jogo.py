# -*- coding: utf-8 -*-
from __future__ import division
import math

Cv= input('digite o numero de vitorias:')
Ce= input('digite o numero de empate:')
Cs= input('digite o saldo de gols:')
Fv= input('digite o numero de vitorias:')
Fe= input('digite o numero de empatess:')
Fs= input('digite o saldo de gols:')

N1= Cv+Ce+Cs
N2= Fv+Fe+Fs

if N1>N2:
    print 'C'
if N2> N1:
    print 'F'
if N1==N2:
    print '='