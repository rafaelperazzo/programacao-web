# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
n = int(input('insira n:'))
notas =[]
for i in range (0,n,1):
    notas.append(float(input('digite a nota%d: ' %(i + 1))))
dh = 0
for i in range (0,n,1)  :
    dh = dh + 1.0 / notas [i]
    
mediah = n/ dh

print (mediah)