# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('Digite o numero de alunos: '))
notas=[]
for i in range(1,n+1,1):
    notas.append(float(input('Digite a nota do {}aluno: '.format(i))))
    a=notas[i]    
if notas>a:
    maior=a
if notas<a:
    menor=a
print(maior,menor)    