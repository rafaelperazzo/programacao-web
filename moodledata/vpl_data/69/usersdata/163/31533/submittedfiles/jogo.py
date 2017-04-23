# -*- coding: utf-8 -*-
import math
CV=int(input('Digite o nº de vitorias de cormengo:'))
CE=int(input('Digite o nº de mepates de cormengo:'))
CS=int(input('Digite o nº do saldo de gols de cormengo:"))

FV=int(input('Digite o nº de vitorias de flaminthians:'))
FE=int(input('Digite o nº de empates de flaminthians:'))
FS=int(input('Digite o nº de gols do flaminthians:'))

if CV>FV:
    print('e')
    elif CV<FV:
    print('F')
 else:
    if CE>FE:
    print('C')
elif CE<FE
    print('F')
else:
    if CS>FS:
    print('C')
elif CS<FS:
    print ('F')
else:
    print('=')