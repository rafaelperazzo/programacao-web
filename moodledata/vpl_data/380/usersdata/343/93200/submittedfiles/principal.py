# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
n = int(input('digite um número: '))
notas = []
for i in range(0,n,1):
    notas.append(float(input('Digite a nota%d: ' % (i+1))))
media = 0
for i in range(0,n,1):
    media += notas[i]/float(n)
for i in range(1,n,1):
    print(notas[i])
print(media)