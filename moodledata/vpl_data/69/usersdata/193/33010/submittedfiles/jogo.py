# -*- coding: utf-8 -*-
CV=int(input('Digite a quantidade de vitórias do cormengo:'))
CE=int(input('Digite a quantidade de empates do cormengo:'))
CS=int(input('Digite o saldo do gols cormengo:'))
FV=int(input('Digite a quantidade de vitórias do flaminthians:'))
FE=int(input('Digite a quantidade de empates do flaminthians:'))
FS=int(input('Digite o saldo de gols do flaminthians:'))
PC=(CV+3)+CE
PF=(FV*3)+FE
if PC>PF:
    print('C')
elif PF>PC:
    print('F')
else:
    if CS>FS:
        print('C)
    elif FS>CS:
        print('F')
    else:
        print('=')