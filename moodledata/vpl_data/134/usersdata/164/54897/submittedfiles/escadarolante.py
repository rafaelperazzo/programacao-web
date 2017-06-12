# -*- coding: utf-8 -*-
n=int(input('Digite o número de pessoas: '))
t=0
for i in range (1, n+1, 1):
    tempo=int(input('Digite o instante em que a pessoa passou pelo sensor da escada rolante: '))
    if (i==0):
        tempo1=t
    elif (i==n):
        tempo2=t
tempo=tempo2-tempo1+10        
print(tempo)    