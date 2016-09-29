# -*- coding: utf-8 -*-
from __future__ import division
import math

vitoriaC = input (' digite o número de vitórias do Cormengo: ')
empateC = input (' digite o número de empates do Cormengo: ')
saldoDeGolC = input (' digite o saldo de gols do Cormengo: ')

vitoriaF = input (' digite o número de vitórias do Flarinthians: ')
empateF = input (' digite o número de empates do Flarinthians: ')
saldoDeGolF = input (' digite o saldo de gols do Flarinthians: ')

totalVitoriaC = vitoriaC * 3
totalEmpateC = empateC * 1

totalVitoriaF = vitoriaF * 3
totalEmpateF = empateF * 1

saldoTotalC = saldoDeGolC
saldoTotalF = saldoDeGolF

totalC = totalVitoriaC + totalEmpateC + saldoTotalC
totalF = totalVitoriaF + totalEmpateF + saldoTotalF

if totalC > totalF:
    print ('C')
    
elif totalC < totalF:
    print ('F')

elif totalC == totalF and saldoTotalC > saldoTotalF:
    print ('C')
    
elif totalC == totalF and saldoTotalC < saldoTotalF:
    print ('F')
    
elif totalC == totalF and saldoTotalC == saldoTotalF:
    print ('=')