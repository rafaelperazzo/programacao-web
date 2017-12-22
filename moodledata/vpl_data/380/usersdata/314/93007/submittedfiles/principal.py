# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('Digite n: '))
if n>1:
notas=[n]
for i in range(0,n,1):
    notas.append(float(input('Digite a nota{}: '.format(i+1))))
media=0
for i in range(0,n,1):
        media += notas[i]/50.0
print(notas)
print(media)