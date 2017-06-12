# -*- coding: utf-8 -*-
n=int(input('Digite o número de pessoas: '))
t=0
a=0
for i in range (1, n+1, 1):
    tempo=int(input('Digite o instante em que a pessoa passou pelo sensor da escada rolante: '))
    t=t+10
    if (tempo-10>t):
        t=(tempo-t)+10
print(t)    