# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
sim = int(input("Quantas notas você deseja ler? ))
notas = []
for i in range (0,sim,1):
    notas.append(float(input('Digite a nota%d: ' % (i+1))))
media = 0
for i in range(0,sim,1):
    media += notas[i]/5.0
print(notas)
print(media)
