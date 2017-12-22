# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
notas=[]
n=int(input('Numero de notas: '))
while n<1:
    n=int(input('Numero de notas: '))
    
for i in range(0,n,1):
    notas.append(float(input('Digite a nota %d: ' %(i+1))))
    media = 0
    for i in range(0,n,1):
        media+=nota[i]/(float(n))
    
print(nota)
print(media)
    