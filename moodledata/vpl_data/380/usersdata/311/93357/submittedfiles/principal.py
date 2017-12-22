# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
x=int(input('Digite o numero de notas: '))
while x<=1:
    x=float(input('Digite o numero de notas: '))
notas = []
for i in range (0,x,1):
    notas.append(float(input('Digite a nota%d: ' % (i+1))))
for i in range (0,x,1):
    denominador =+ (1/(notas[i]))

mediah= ((x)/denominador**-1)
print (mediah)
    