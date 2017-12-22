# -*- coding: utf-8 -*-

n = int(input('Digite o numero de alunos: '))

notas = [ ]

for i in range(0, n, 1):
    notas.append(float(input('Digite a nota do {}º aluno: '.format(i+1))))
    
maior = notas[0]
menor = notas[0]

for i in range(0, n, 1) :
    if (notas[i] > maior) :
        maior = notas[i]
    if (notas[i] < menos) :
        menor = notas[i]
      
      
print(maior, "\n")        
print(menor, "\n")
      