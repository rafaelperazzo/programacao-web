# -*- coding: utf-8 -*-
n = int(input('Digite a quantidade de alunos: '))

idade = []
for i in range (0,n,1):
    idade.append(int(input('Qual a idade do %dº aluno: ' %(i + 1))))
    if idade[i] < 18 or idade[i] == -1:
        break
    
altura = []
for j in range (0,n,1):
    altura.append(float(input('Qual a altura do %dº aluno: ' %(j + 1))))
    if altura[j] < 0:
        break
    
media_alturas = (sum(altura))/n

cont = 0
for i in range (0,n,1):
    for j in range (0,n,1):
        if idade[i] > 25 and altura[j] > media_alturas:
    cont = cont + 1

print(cont)    