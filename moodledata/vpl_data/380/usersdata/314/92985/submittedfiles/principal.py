# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=float(input('Digite n: '))
notas=[n]
for i in range(0,n,1):
    notas.append(float(input('Digite a nota{}: '.format(i+1))))
media=0
for i in range(0,n,1):
        media += notas[i]/50.0
print(notas)
print(media)