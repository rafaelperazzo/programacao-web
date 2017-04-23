# -*- coding: utf-8 -*-
import math
CV=int(input('escreva a quantidade de vitórias do cormengo:'))
CE=int(input('escreva a quantidade de empates do cormengo:'))
CS=int(input('escreva o saldo de gols do cormengo:'))
FV=int(input('escreva a quantidade de vitórias do flaminthias:'))
FE=int(input('escreva a quantidade de empates do flaminthias:'))
FS=int(input('escreva o saldo de gols do flaminthias:'))
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
        print('F)
    else:
        print('=')

