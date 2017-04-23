# -*- coding: utf-8 -*-
import math
CV=int(input('Escreva a quantidade de vitorias do cormengo:'))
CE=int(input('Escreva a quantidade de empates do cormengo:'))
CS=int(input('Escreva o saldo de gols do cormengo:'))
FV=int(input('Escreva a quantidade de vitorias do flaminthias:'))
FE=int(input('Escreva a quantidade de empates do flaminthias:'))
FS=int(input('Escreva o saldo de gols do flaminthias:'))

PC=(CV*3)+CE
PF=(FV*3)+FE

if PC>PF:
    print('C')
elif PF>PC:
    print('F')
else:
    if CS>FS:
        print('C')