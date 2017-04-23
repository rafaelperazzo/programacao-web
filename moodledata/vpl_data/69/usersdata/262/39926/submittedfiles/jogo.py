# -*- coding: utf-8 -*-
import math

CV=int(input('Digite o numero de vitorias do Cormengo:'))
CE=int(input('Digite o numero de empates do Cormengo:'))
CS=int(input('Digite o numero do saldo de gols do Cormengo:'))

FV=int(input('Digite o numero de vitorias do Flaminthians:'))
FE=int(input('Digite o numero de empates do Flaminthians:'))
FS=int(input('Digite o numero de saldo de gols do Flaminthians:'))


V1=CV*3+CE+1
V2=FV*3+FE+1

if V1>V2:
    print('C')
elif V1<V2:
    print('F')
else:
    if CS>FS:
        print('C')
    
    elif CS<FS:
        print('F')
    
    else:
        print('=')