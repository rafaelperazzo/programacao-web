# -*- coding: utf-8 -*-
x = 50
notas = []
for i in range(0,x,1):
    notas.append(float(input('Digite a nota%d[%d]: '% (i+1, i))))
media = 0
somatorio = 0
for i in range(0,x,1):
    somatorio += notas[i]
print(notas)
media = somatorio/x
print(media)