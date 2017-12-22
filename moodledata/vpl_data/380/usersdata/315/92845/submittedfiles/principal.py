# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
notas =[]
for i in range(0,50,1):
    notas.append(float(input('digite nota %d: ' %(i+1))))
media = 0
for i in range (0,50,1):
    media+= notas[i]/50.0
print (notas)
print (media)

