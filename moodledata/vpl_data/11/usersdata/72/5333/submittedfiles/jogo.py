# -*- coding: utf-8 -*-
from __future__ import division
import math
#ENTRADA
cv=input ('digite a quantidade de vitorias do cormengo:')
ce=input ('digite a quantidade de empates do cormengo:')
cs=input ('diigite a quantidade do saldo de gols do cormengo:')
fv=input ('digite a quantidade de vitorias do flaminthians:')
fe=input ('digite a quantidade de empates do flaminthians:')
fs=input ('digite a quantidade do saldo de gols do flaminthians:')

#PROCESSAMENTO
pc=(cv*3)+ce
pf=(fv*3)+fe

#SAIDA
if pc>pf or cs>fs:
    print ('C')
if pc<pf or cs<fs:
    print ('F')
else:
    print ('=')