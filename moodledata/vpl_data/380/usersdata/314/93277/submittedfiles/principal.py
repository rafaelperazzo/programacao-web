# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('Digite n: '))
notas=[]
for i in range(0,n,1):
    notas.append(float(input('Digite a nota{}: '.format(i+1))))
mediaH=0
for i in range(0,n,1):
        mediaH += notas[i]/sum(float(notas*(1/i)))
        print(notas[i])
print(mediaH)