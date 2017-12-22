# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#ENTRADA
notas = []
for i in range (0,50,1):
    notas.append(float(input('Digite a nota %d: ' % (i+1))))
media = 0
for i in range(0,5,1):
    media += notas[i]/5.0
print(notas)
print(media)