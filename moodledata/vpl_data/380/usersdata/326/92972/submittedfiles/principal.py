1# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
import random
n = int(input('digite a quantidade de alunos: '))

notas = []
for i in range(0,n,1):
    notas.append(random.randint(0,10))
media=0
for i in range(0,n,1):
    media += notas[i]/n
print(notas)
print(media)