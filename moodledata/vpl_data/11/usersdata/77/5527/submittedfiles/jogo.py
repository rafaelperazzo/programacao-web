# -*- coding: utf-8 -*-
from __future__ import division
import math

cv=input('Digite o número de vitórias do Cormengo:')
ce=input('Digite o número de empates do Cormengo:')
cs=input('Digite o número do saldo de gols do Cormengo:')
fv=input('Digite o número de vitórias do Flaminthians:')
fe=input('Digite o número de empates do Flaminthians:')
fs=input('Digite o número do saldo de gols do Flaminthians:')

npc=(cv*3)+(ce*1)
npf=(fv*3)+(fe*1)

if npc>npf:
    print('C')
elif npc<npf:
    print('F')
if npc==npf:
    print('=')

