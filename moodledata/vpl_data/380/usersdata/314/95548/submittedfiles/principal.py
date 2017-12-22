# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('Digite o numero de alunos: '))
for i in range(1,n+1,1):
    notas=float(input('Digite a nota do aluno: '))
    if notas>0:
        notas=maior
        maior+=1
    if maior==1:
        maior=notas
        print(maior)
    if notas>0:
        notas=menor
        menor+=1
    if menor==1:
        print(menor)
