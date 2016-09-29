# -*- coding: utf-8 -*-
from __future__ import division
import math

Cv=input('Digite o número de vitórias do cormengo:')
Ce=input('Digite o número de empates do cormengo:')
Cs=input('Digite o saldo de gols do cormengo:')
Fv=input('Digite o número de vitórias do flaminthias:')
Fe=input('Digite o número de empates do flaminthias:')
Fs=input('Digite o saldo de gols do flaminthias:')

Pc=(Cv*3)+(Ce*1)
Pf=(Fv*3)+(Fe*1)

if Pc>Pf or Cv>Fv or Cs>Fs:
    print('C')
elif Pf>Pc or Fv>Cv or Fs>Cs:
        print('F')
elif Pc==Pf and Cv==Fv and Cs==Fs:
        print('=')


