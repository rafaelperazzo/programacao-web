# -*- coding: utf-8 -*-
from __future__ import division
import math
Cv=input('Insira o número de vitórias do Cormengo')
Ce=input('Insira o número de empates do cormengo')
Cs=input('Insira o saldo de gols do cormengo')
Fv=input('Insira o número de vitórias do Cormengo')
Fe=input('Insira o número de empates do cormengo')
Fs=input('Insira o saldo de gols do cormengo')
pc=(3*cv)+ce
pf=(3*fv)+fe
if pc>pf:
    print:('C')
if pc<pf:
    print:('F')
if pc==pf:
    if cs>fs:
        print:('C')
    if cs<fs:
        print:('f')
    if cs==fs:
        print('=')