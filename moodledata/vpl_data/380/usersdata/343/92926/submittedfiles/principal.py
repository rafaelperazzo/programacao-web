# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
notas = []
for i in range(0,50,1):
    notas.append(float(input('Digite a nota%d: ' % (i+1))))
for i in range(0,50,1):
    media += notas[i]/50.0
print(notas)
print(media)