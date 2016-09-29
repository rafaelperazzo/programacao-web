# -*- coding: utf-8 -*-
from __future__ import division
import math

CV=('Número de vitórias co Cormengo:')
CE=('Número de empates do Cormengo:')
CS=('Número de saldo de gols do Cormengo:')
FV=('Número de vitórias co Flaminthias:')
FE=('Número de empates do Flaminthias:')
FS=('Número de saldo de gols do Flaminthias:')

NPC=((CV*3)+(CE*1))
NPF=((FV*3)+(FE*1))

if NPC>NPF:
    print('C')
if NPF>NPC:
    print('F')
if NPC==NPF:
    elif CS>FS:
        print('C')
    elif FS>CS:
        print('F')
    else:
        print('=')