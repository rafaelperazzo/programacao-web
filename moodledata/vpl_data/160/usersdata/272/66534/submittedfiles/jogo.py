# -*- coding: utf-8 -*-
import math

Cv= int(input('Digite o número de vitórias do Cormengo:'))
Ce= int(input('Digite o número de empates do Cormengo:'))
Cs= int(input('Digite o saldo de gols do Cormengo:'))
Fv= int(input('Digite o número de vitórias do Flaminthians:'))
Fe= int(input('Digite o número de empates do Flaminthians:'))
Fs= int(input('Digite o saldo de gols do Flaminthians:'))

PontosC= (3*Cv)+Ce
PontosF= (3*Fv)+Fe

if (PontosC>PontosF):
    print('C')

elif (PontosF>PontosC):
    print('F')
    
elif (PontosC==PontosF) and (Cs>Fs):
    print('C')

elif (PontosC==PontosF) and (Fs>Cs):
    print('F')

elif (PontosC==PontosF) and (Cs==Fs):
    print('=')

