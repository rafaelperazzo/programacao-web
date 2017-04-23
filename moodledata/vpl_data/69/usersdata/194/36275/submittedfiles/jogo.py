# -*- coding: utf-8 -*-
import math
CV=int(input('Digite a quantidade de vitórias do Cormengo:'))
CE=int(input('Digite a quantidade de empates do Cormengo:'))
CS=int(input('Digite o valor de gols  do Cormengo:'))
CV=int(input('Digite a quantidade de vitórias do Flaminthians:'))
CE=int(input('Digite a quantidade de empates do Flaminthians:'))
CS=int(input('Digite o saldo de gols do Flaminthians:'))

PC=(VC*3)+CE
PF=(FV*3)+FE

if PC>PE:
    print('c')
elif PF>PC:
    print('F')
else:
    if CS>FS:
        print('C')
    elif FS>CS:
        print('F')
else:
    print('m')