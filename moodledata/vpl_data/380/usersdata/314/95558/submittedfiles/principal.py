# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('Digite o numero de alunos: '))
notas=[]
for i in notas(1,n+1,1):
    notas.append(float(input('Digite a nota do {}aluno: '.format(i))))
    maior=notas[0]
    if i>maior:
        maior=i
print(maior)        
      