# -*- coding: utf-8 -*-
import math
#Entrada:
cv= int(input('Digite o número de vitórias do Cormengo:'))
ce= int(input('Digite o número de empates do Cormengo:'))
cs= int(input('Digite o saldo de gols do Cormengo:'))
fv= int(input('Digite o número de vitórias do Flaminthians:'))
fe= int(input('Digite o número de empates do Flaminthians:'))
fs= int(input('Digite o saldo de gols do Flaminthians:'))
#Processamento e Saída:
pc= (cv*3)+ ce 
pf= (fv*3)+ ce
if (pc>pf):
    print('C')
if (pf>pc):
    print('F')
if (pf==pc) and (cs>fs):
    print ('C')
if (pf==pc) and (fs>cs):
    print ('F')
if (pf==pc) and (cs==fs):
    print ('=')