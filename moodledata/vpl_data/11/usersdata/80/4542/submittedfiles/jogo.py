# -*- coding: utf-8 -*-
from __future__ import division
import math

CV=int(input('digite o numero de vitorias do Cormengo:'))
CE=int(input('digite o numero de empates do Cormengo:'))
CS=int(input('digite o saldo de gols do Cormengo:'))
FV=int(input('digite o numero de vitorias do Flaminthians:'))
FE=int(input('digite o numero de empates do Flaminthians:'))
FS=int(input('digite o saldo de gols do Flaminthians:'))
CP=(3*CV)+CE
FP=(3*FV)+FE
if CP>=FP and CS>FS:
    print