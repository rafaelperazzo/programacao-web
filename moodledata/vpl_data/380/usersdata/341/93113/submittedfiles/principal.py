# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
n=int(input('Digite a quantidade de notas: '))
notas = []
for i in range (0,n,1):
    notas.append(float(input('Digite a nota%d: ' % (i+1))))
print(notas)
media=sum(notas)/len(notas)
print(media)
