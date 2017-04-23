# -*- coding: utf-8 -*-
import math
CV=int(input('Digite a quantidade de vitórias do Cormengo:'))
CE=int(input('Digite a quantidade de empates do Cormengo:'))
CS=int(input('Digite o valor de gols  do Cormengo:'))
FV=int(input('Digite a quantidade de vitórias do Flaminthians:'))
FE=int(input('Digite a quantidade de empates do Flaminthians:'))
FS=int(input('Digite o saldo de gols do Flaminthians:'))

PC=(CV*3)+CE
PF=(FV*3)+FE

if PC>PF:
    print('c')
elif PF>PC:
    print('F')
else:
    if CS>FS:
        print('C')
    elif FS>CS:
        print('F')
    else:
        print('=')