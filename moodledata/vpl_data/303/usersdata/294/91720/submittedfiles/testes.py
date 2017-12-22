# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
notas = []
n = int(input("Digite o número de notas: "))
while (n<1):
    n = int(input("Digite o número de notas: "))
for i in range(0,n,1):
    notas.append(float(input('Digite nota%d: ' % (i+1))))
média = sum(notas)/n
