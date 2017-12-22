# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
n = int(input('Digite o número de notas: '))
notas  = []
for i in range (0,n,1):
    notas.append(float(input('Digite a nota %d: ' %(i + 1))))
media = 0
for i in range (0,n,1):
    media += notas[i]/n
    print(notas[i])
print(media)
