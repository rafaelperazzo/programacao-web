# -*- coding: utf-8 -*-
import random
#COMECE AQUI ABAIXO
n=int(input('Digite a quantidade de notas: '))
notas = []
for i in range(0,n,1): 
    notas.append(random.randint(0,10))
media=0
for i in range (0,n,1):
    media += notas[i]/n
    print(notas[i])
print(media)
