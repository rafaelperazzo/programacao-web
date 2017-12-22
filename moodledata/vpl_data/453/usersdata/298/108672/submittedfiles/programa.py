# -*- coding: utf-8 -*-
n=int(input('Digite a dimensao da matriz: '))
while n<3:
    n=int(input('Entrada invalida. n deve ser maior ou igual a 3: '))

m=[]
for i in range (0, n, 1):
    linha=[]
    for j in range (0, n, 1):
        linha.append(int(input('Digite o valor da casa no tabuleiro: ')))
    m.append(linha)

linhas=[]
for i in range (0, n, 1):
    linhas.append(sum(m[i]))

colunas=[]
for i in range (0, n, 1):
    k=0
    for j in range (0, n, 1):
        k+=m[j][i]
    colunas.append(k)

b=[]
for i in range (0, n, 1):
    l=[]
    p=0
    q=0
    for j in range (0, n, 1):
        p=linhas[i]-m[i][j]
        q=colunas[j]-m[i][j]
        l.append(p+q)
    b.append(l)

maior=0
for i in range (0, n, 1):
    for j in range (0, n, 1):
        if b[i][j]>maior:
            maior=b[i][j]

print(maior)