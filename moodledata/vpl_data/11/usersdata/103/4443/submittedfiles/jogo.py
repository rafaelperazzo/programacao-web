# -*- coding: utf-8 -*-
from __future__ import division
import math
Cv=input('Insira o número de vitórias do Cormengo')
Ce=input('Insira o número de empates do cormengo')
Cs=input('Insira o saldo de gols do cormengo')
Fv=input('Insira o número de vitórias do Cormengo')
Fe=input('Insira o número de empates do cormengo')
Fs=input('Insira o saldo de gols do cormengo')
pc=(3*Cv)+Ce
pf=(3*Fv)+Fe
if pc>pf:
    print('C')
if pc<pf:
    print('F')
if pc==pf:
    if Cs>Fs:
        print('C')
    if Cs<Fs:
        print('F')
    if Cs==Fs:
        print('=')