import numpy as np

# inicializando matriz vazia 5x3
linhas = 5
colunas = 3
turma = np.empty([linhas,colunas])

# lendo três notas de cinco alunos
for i in range(0,linhas,1):
    for j in range(0,colunas,1):  
        turma[i][j] = float(input('Digite a nota%d do aluno%d: ' % ((j+1),(i+1))))

# mostrando toda a matriz de notas
print(turma)	