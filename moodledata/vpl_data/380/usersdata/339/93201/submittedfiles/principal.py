# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
a=[]
for i in range(1,11,1):
    a.append(input('elemento: '))
for i in range(9,-1,-1):
    print(a[i])




n=int(input('Numero de notas: '))
while n<1:
    n=int(input('Numero de notas: '))
notas=[]  
for i in range(0,n,1):
    notas.append(float(input('Digite a nota %d: ' %(i+1))))
media = 0
for i in range(0,n,1):
    print(notas[i])
    









