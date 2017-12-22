# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('Digite o numero de alunos: '))
notas=[]
for i in range(1,n+1,1):
    notas.append(float(input('Digite a nota do {}aluno: '.format(i))))
for i in range(1,n+1,1):
    maior=notas[0]
    if maior>i:
        maior=i
print(maior)        
      