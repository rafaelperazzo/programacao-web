# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
n = int(input('insira n:'))
notas =[]
for i in range (0,n,1):
    notas.append(float(input('digite a nota%d: ' %(i + 1))))
for i in range (0,n,1)  :
    print (notas[i])