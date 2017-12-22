# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
x=float(input('Digite o numero de notas: '))
notas = []
for i in range (0,x,1):
    notas.append(float(input('Digite a nota%d: ' % (i+1))))
media = 0
for i in range (0,x,1):
    media += notas [i]/x
print (notas)
print (media)