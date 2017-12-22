import numpy as np

# inicializando matriz vazia 5x3
turma = np.empty([5,3])

print(len(turma))

# lendo três notas de cinco alunos
for i in range(0,5,1):
    for j in range(0,3,1):  
        turma[i][j] = float(input('Digite a nota%d do aluno%d: ' % ((j+1),(i+1))))

# mostrando toda a matriz de notas
print(turma)

"""
from minha_bib import *
# -*- coding: utf-8 -*-
a = [8.0, 5.0, 10.0, 5.0]
print(a)
print(len(a))
# 2.0 na posicao 2 (indice 1)
inserir(a,10.0,0)
print(a)
print(len(a))
"""