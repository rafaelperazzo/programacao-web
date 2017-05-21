# -*- coding: utf-8 -*-
n = int(input('Digite o número de pessoas: '))
tI = int(input('Digite o tempo que a pessoa 1 passou: '))
tempoTotal=10
for i in range(2,n+1,1):
    t = int(input('Digite o tempo que a pessoa '+str(i)+' passou: '))
    tF=t-tI
    tempoTotal=tempoTotal+tF
    tI=t
print(tempoTotal)    