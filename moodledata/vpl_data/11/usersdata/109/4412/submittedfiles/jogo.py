# -*- coding: utf-8 -*-
from __future__ import division
import math

CV=input('Número de vitórias co Cormengo:')
CE=input('Número de empates do Cormengo:')
CS=input('Número de saldo de gols do Cormengo:')
FV=input('Número de vitórias co Flaminthias:')
FE=input('Número de empates do Flaminthias:')
FS=input('Número de saldo de gols do Flaminthias:')

NPC=((CV*3)+(CE*1))
NPF=((FV*3)+(FE*1))

if NPC>NPF:
    print('C')
if NPF>NPC:
    print('F')
if NPC==NPF:
    if CS>FS:
        print('C')
    elif FS>CS:
        print('F')
    else:
        print('=')