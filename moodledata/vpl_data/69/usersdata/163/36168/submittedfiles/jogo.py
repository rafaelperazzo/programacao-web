# -*- coding: utf-8 -*-
import math

CV=int(input('Digite o nº de vitorias de Cormengo:'))
CE=int(input('Digite o nº de mepates de Cormengo:'))
CS=int(input('Digite o nº do saldo de gols de Cormengo:'))

FV=int(input('Digite o nº de vitorias de Flaminthians:'))
FE=int(input('Digite o nº de empates de Flaminthians:'))
FS=int(input('Digite o nº de gols do Flaminthians:'))


v1=CV*3+CE*1
v2=FV*3+FE*1

if v1>v2:
    print('C')
    
elif v1<v2:
    print('F')
    
else:
    if CS>FS:
        print('C')
    
    elif CS<FS:
        print('F')
        
    else:
        print ('=')
        