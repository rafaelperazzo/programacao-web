# -*- coding: utf-8 -*-
from __future__ import division
import math
#ENTRADA
cV = input('N vitorias do Cormengo:')
cE = input('N de empates do cormengo ')
cS = input('Saldo de Gols do Cormengo ')
fV = input('N vitorias do Flaminthias:')
fE = input('N de empates do Flaminthias ')
fS = input('Saldo de Gols do Flaminthias ')
#PROCESSAMENTO
pontosVitoriasC = cV*3
pontosEmpateC = cE*1
pontosTotaisC = pontosVitoriasC + pontosEmpateC
pontosVitoriasF = fV*3
pontosEmpateF = fE*1
pontosTotaisF = pontosVitoriasF + pontosEmpateF

if pontosTotaisC>pontosTotaisF:
    print('C')
elif pontosTotaisF>pontosTotaisC:
    print('F')
elif cS>fS:
    print('C')
elif fS>cS:
    print('F')
elif cS==fS:
    print('=')

