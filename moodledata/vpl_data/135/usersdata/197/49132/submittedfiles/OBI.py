# -*- coding: utf-8 -*-
n=int(input('Digite o numero total de participantes:'))
p=float(input('Digite a nota minima a ser alcançada:'))
participantes=0
cont=0
while cont<n:
    x=float(input('Digite a nota da primeira fase:'))
    y=float(input('Digite a nota da segunda fase:'))
    if x+y>=p:
        participantes=participantes+1
    cont=cont+1
print(participantes)