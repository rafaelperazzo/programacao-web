# -*- coding: utf-8 -*-
n=int(input('Digite o número de pessoas: '))
t=0
for i in range (1, n+1, 1):
    tempo=int(input('Digite o instante em que a pessoa passou pelo sensor da escada rolante: '))
    if (i==1):
        tempo1=tempo
    elif (i==n):
        tempo2=tempo
t=tempo2-tempo1+10        
print(t)    