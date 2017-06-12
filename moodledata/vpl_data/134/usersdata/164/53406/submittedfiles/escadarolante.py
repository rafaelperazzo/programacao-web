# -*- coding: utf-8 -*-
n=int(input('Digite o número de pessoas: '))
t=0
for i in range (1, n+1, 1):
    tempo=int(input('Digite o instante em que a pessoa passou pelo sensor da escada rolante: '))
    t=t+10
print(t)    