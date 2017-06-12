# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
tempo=10
n=int(input('Digite o número de pessoas: '))
for i in range(1,n+1,1):
    t=int(input('Digite o tempo em que a pessoa '+str(i)+' passou: '))
    if (tempo-t)>tempo:
        tempo=tempo+(tempo-t)
print(tempo)        