# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('Digite o numero de alunos: '))
notas=[]
for i in range(1,n+1,1):
    notas.append(float(input('Digite a nota do {}aluno: '.format(i))))
for c in range(1,n+1,1):    
    notas[c+1]
    if notas>notas[c+1]:
        maior=notas
    if notas<notas[c+1]:
        menor=notas
print(maior,menor)    