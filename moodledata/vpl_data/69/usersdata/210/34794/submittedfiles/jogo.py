# -*- coding: utf-8 -*-
CV=int(input('DIGITE O TOTAL DE VITÓRIAS DO CORMENGO:'))
CE=int(input('DIGITE O TOTAL DE EMPATES DO CORMENGO:'))
CS=int(input('DIGITE O SALDO DE GOLS DO CORMENGO:'))
FV=int(input('DIGITE O TOTAL DE VITÓRIAS DO FLAMINTHIAS:'))
FE=int(input('DIGITE O TOTAL DE EMPATES DO FLAMINTHIAS:'))
FS=int(input('DIGITE O SALDO DE GOLS DO FLAMINTHIAS:'))
PC=(CV*3)+CE
PF=(FV*3)+FE
if PC>PF:
    PRINT('C')
elif PF>PC:
    PRINT('F')
else:
    if CS>FS:
        PRINT('C')
    elif FS>CS:
        PRINT('F')
    else:
        print('=')



