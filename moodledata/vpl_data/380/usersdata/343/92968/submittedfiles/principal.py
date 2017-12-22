# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
n = int(input('digite um número: '))
notas = []
for i in range(0,n,1):
    notas.append(float(input('Digite a nota%d: ' % (i+1))))
for i in range(0,n,1):
    media += notas[i]/n
print(notas)
print(media)