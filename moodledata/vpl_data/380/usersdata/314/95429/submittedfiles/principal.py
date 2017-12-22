# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('Digite o numero de alunos: '))
notas=[]
for i in range(1,n+1,1):
    notas.append(float(input('Digite a nota do {}aluno: '.format(i))))
for i in range(1,n+1,1):
    a=float(notas[i])
    if a>float(notas):
        maior=a
    if a<float(notas):
        menor=a
        