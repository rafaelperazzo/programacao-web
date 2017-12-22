# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
x=int(input('Digite o numero de notas: '))
while x<=1:
    x=float(input('Digite o numero de notas: '))
notas = []
for i in range (0,x,1):
    notas.append(input('Digite a nota: '))
for i in range (0,x,1):
    if notas[x] %2 == 0:
        print (notas[i])
    
 