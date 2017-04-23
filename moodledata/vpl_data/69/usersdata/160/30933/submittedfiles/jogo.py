# -*- coding: utf-8 -*-
import math

cv=int(input('Digite o numero de vitorias do Cormengo: '))
CE=int(input('Digite o numero de empates do Cormengo: '))
CS=int(input('Digite o numero do saldo de gols do Cormengo: '))

fv=int(input('Digite o numero de vitorias do Flaminthians: '))
FE=int(input('Digite o numero de empates do Flaminthians: '))
FS=int(input('Digite o numero do saldo de gols do Flaminthians: '))

CV=cv*3
FV=fv*3

if CV>FV:
    print('C')

elif CV<FV:
    print('F')
    
else:
    if CE>FE:
        print('C')
    
    elif CE<FE:
        print('F')
        
    else:
        if CS>FS:
            print('C')
        
        elif CS<FS:
            print('F')
        
        else:
            print('=')
