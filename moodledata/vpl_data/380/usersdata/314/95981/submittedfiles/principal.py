# -*- coding: utf-8 -*-

n = int(input('Digite o numero de alunos: '))

notas = [ ]

for i in range(1, n+1, 1):
    notas.append(float(input('Digite a nota do {}º aluno: '.format(i))))
    
maior = notas[1]

for i in range(1, n+1, 1) :
    if (notas[i] > maior) :
      maior = notas[i]
      
print(maior)        
      