# -*- coding: utf-8 -*-
import math
CV= int(input('digite a quantidade de vitorias do cormengo:'))
CE= int(input('digite a quantidade de empates do cormengo:'))
CS= int(input('digite o saldo de gols do cormengo:'))
FV= int(input('digite a quantidade de vitorias do flaminthians:'))
FE= int(input('digite a quantidade de empates do flaminthians:'))
FS= int(input('digite o saldo de gols do flaminthians:'))
PC= (CV*3)+CE
PF= (FV*3)+FE
if PC>PF:
    print('C')
elif pf>pc:
    print('F')
else:
    if CS>FS:
        print('C')
    elif FS>CS:
        print('F')
    else:
        print('=')