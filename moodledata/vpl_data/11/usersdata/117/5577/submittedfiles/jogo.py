# -*- coding: utf-8 -*-
from __future__ import division
import math

Cv=input('Digite o número de vitórias do Cormengo:')
Ce=input('Digite o número de empates do Cormengo:')
Cs=input('Digite o saldo de gols do Cormengo:')
Fv=input('Digite o número de vitórias do Flaminthias:')
Fe=input('Digite o número de empates do Flaminthias:')
Fs=input('Digite o saldo de gols do Flaminthias:')

C=(Cv*3)+(Ce*1)
F=(Fv*3)+(Fe*1)

if C>F:
    print('C')
if C<F:
    print('F')
if C==F:
    if Cs>Fs:
        print('C')
    if Cs<Fs:
        print('F')
    if Cs==Fs:
        print('=')