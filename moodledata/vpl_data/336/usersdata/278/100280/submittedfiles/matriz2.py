# -*- coding: utf-8 -*-
n = int(input("Digite a dimensão da matriz: "))
matriz = np.empty([n,n])
for i in range (0,n,1):
    for j in range (0,n,1):
        turma[i][j].append(int(input("Digite o elemento da linha%.d e coluna%.d: " %(i,j))))
soma=0
for i in range (0,n,1):
    soma+=turma[i]
print(soma)

