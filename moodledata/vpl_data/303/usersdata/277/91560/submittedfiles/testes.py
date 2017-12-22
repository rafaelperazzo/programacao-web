# -*- coding: utf-8 -*-
notas = []
for i in range(0,5,1):
    notas.append(float(input('Digite a nota%d[%d]: '% (i+1, i))))
media = 0
somatorio = 0
for i in range(0,5,1):
    somatorio += notas[i]
print(notas)
media = somatorio/5.0
print(media)