# -*- coding: utf-8 -*-
import math
CV=int(input('DIGITE O TOTAL DE VITÓRIAS DO CORMENGO:'))
CE=int(input('DIGITE O TOTAL DE EMPATES DO CORMENGO:'))
CS=int(input('DIGITE O SALDO DE GOLS DO CORMENGO:'))
FV=int(input('DIGITE O TOTAL DE VITÓRIAS DO FLAMINTHIAS:'))
FE=int(input('DIGITE O TOTAL DE EMPATES DO FLAMINTHIAS:'))
FS=int(input('DIGITE O SALDO DE GOLS DO FLAMINTHIAS:'))
PC=(CV*3)+CE
PF=(FV*3)+FE
if PC>PF:
    print('C')
elif PF>PC:
    print('F')
else:
    if CS>FS:
        print('C')
    elif FS>CS:
        print('F')
    else:
        print('=')
    
