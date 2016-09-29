# -*- coding: utf-8 -*-
from __future__ import division
import math

Cv = input('Digite o número de vitórias do Cormengo:')
Ce = input('Digite o número de empates do Cormengo:')
Cs = input('Digite o saldo de gols do Cormengo:')
Fv = input('Digite o número de vitórias do Flaminthians:')
Fe = input('Digite o número de empates do Flaminthians:')
Fs = input('Digite o saldo de gols do Flaminthians:')

PontosCormengo = (3 * Cv) + (1 * Ce)
PontosFlaminthians = (3 * Fv) + (1 * Fe)
if PontosCormengo > PontosFlaminthians:
    print('C')
elif PontosFlaminthians > PontosCormengo:
    print('F')
elif PontosCormengo == PontosFlaminthians and Cs>Fs:
    print('C')
elif PontosCormengo == PontosFlaminthians and Fs>Cs:
    print('F')
else:
    print('=')