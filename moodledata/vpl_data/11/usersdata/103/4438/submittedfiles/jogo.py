# -*- coding: utf-8 -*-
from __future__ import division
import math
cv=input('Insira o número de vitórias do Cormengo')
ce=input('Insira o número de empates do cormengo')
cs=input('Insira o saldo de gols do cormengo')
fv=input('Insira o número de vitórias do Cormengo')
fe=input('Insira o número de empates do cormengo')
fs=input('Insira o saldo de gols do cormengo')
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