# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
notas = []
n= 5
for i in range(0,n,1):
    notas.append(float(input('Digite nota%d: ' % (i+1))))
media = sum(notas)/len(notas)
print(notas)
print(media)
