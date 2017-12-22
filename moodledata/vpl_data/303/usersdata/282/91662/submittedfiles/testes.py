# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
x= int(input('Quantas notas vc tem? '))
notas = []
for i in range (0,x,1):
    notas.append(float(input('Digite a nota%d[%d]: '% (i+1, i))))
media=0 
somatorio =0
for i in range(0,x,1):
    media += notas[i]/x
print(notas)
print(media)
    