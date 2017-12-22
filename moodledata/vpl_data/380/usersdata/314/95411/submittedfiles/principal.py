# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('Digite o numero de alunos: '))
notas=[]
for i in range(1,n+1,1):
    notas.append(float(input('Digite a nota do {}aluno: '.format(i))))
    a=(notas[i])
    b=(notas[i+1])
    if a>b:
        maior=a
    if b>a:
        menor=a
print(maior,menor)        
   