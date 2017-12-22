# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('Digite o numero de alunos: '))
if n>0:
    maior=notas
else:
    menor=notas
for i in range(1,n+1,1):
    notas=(float(input('Digite a nota do {}aluno: '.format(i))))
    if notas>a:
        notas=maior
    if notas<a:
        notas=menor
print(maior)
print(menor)
