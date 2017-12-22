# -*- coding: utf-8 -*-

n = int(input('Digite o numero de alunos: '))

notas = [ ]

for i in range(1, n+1, 1):
    notas.append(float(input('Digite a nota do {}aluno: '.format(i))))
    
maior = notas[0]

for i in range(1, n+1, 1):
    if notas[i+1] > maior:
      maior = notas[i]
      
print(maior)        
      