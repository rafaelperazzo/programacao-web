# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
n=int(input('Digite o numero de notas: '))
a = []
for i in range (0,n,1):
    a.append(input('Digite a nota: '))
for i in range (0,n,1):
    if (a[i]) %2 == 0:
        print (a[i])
    
 