# -*- coding: utf-8 -*-
import math
CV=int(input('Digite o Número de Vitórias do Cormengo:'))
CE=int(input('Digite o Número de Empates do Cormengo:'))
CS=int(input('Digite o Saldo de Gols do Cormengo:'))
FV=int(input('Digite o Número de Vitórias do Flaminthians:'))
FE=int(input('Digite o Número de Vitórias do Flaminthians:'))
FS=int(input('Digite o Saldo de Gols do Flaminthians:'))
CV=CV*3
FV=FV*3
CT=CV+CE
FT=FV+FE
if (CT>FT):
    print('C')
elif (FT>CT):
    print('F')
else:
    print('=')
    