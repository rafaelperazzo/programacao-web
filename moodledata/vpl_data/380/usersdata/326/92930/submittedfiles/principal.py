1# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
import random
notas = []
for i in range(0,50,1):
    notas.append(random.randint(0,10))
media=0
for i in range(0,50,1):
    media += (notas[i]/5.0)
print(notas)
print(media)