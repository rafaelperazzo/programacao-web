# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('Digite o numero de alunos: '))
for i in range(1,n+1,1):
    notas=(float(input('Digite a nota do {}aluno: '.format(i))))
    a=10
    if notas>a:
        notas=maior
    if notas<a:
        notas=menor
print(maior)
print(menor)
