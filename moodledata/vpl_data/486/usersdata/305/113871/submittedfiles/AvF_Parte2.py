# -*- coding: utf-8 -*-
n = int(input('Digite a quantidade de alunos: '))

idade = []
for i in range (0,n,1):
    idade.append(int(input('Qual a idade do %dº aluno: ' %(i + 1))))
    if idade[i] < 18 or idade[i] == -1:
        break

    