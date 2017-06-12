# -*- coding: utf-8 -*-
n=int(input('Digite o Número de Pessoas que o Sensor Detectou:'))
i=0
for i in range(1,n+1,1):
    t=int(input('Digite o Instante que a I-ésima Pessoa passou pelo Sensor:'))
    if (i==1):
        t1=t
    elif (i==n):
        t2=t
tempo=t2-t1+10
print(tempo)