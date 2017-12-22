# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n = int(input("Digite o número de notas: "))
notas = []
while n<=1:
    n = int(input("Digite o número de notas: "))
for i in range(0,n,1):
    notas.append(float(input("digite a nota%d: " % (i+1)))) 
media = 0
for i in range(0,n,1):
    media += notas[i]/5.0
print(notas)
print(media)