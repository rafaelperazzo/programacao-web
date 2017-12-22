# -*- coding: utf-8 -*-

n=int(input('Digite a dimensão do tabuleiro: '))
m=[]
for i in range (0,n,1):
    m_linha=[]
    for j in range(0,n,1):
        m_linha.append(int(input('Digite o números (%d,%d) de entrada: '% (i+1,j+1))))
    m.append(m_linha)
    
soma_linha=[]
for i in range(0,n,1):
    c=0
    for j in range(0.n,1):
        c=c+m[i][j]
    soma_linha.append(c)
    
soma_coluna=0
for j in range(0,n,1):
    c2=0
    for i in range(0,n,1):
        c2=c2+m[i][j]
    soma_coluna.append(c2)

peça=0
for i in range(0,n,1):
    for j in range(0,n,1):
        if (soma_linha[i]+soma_coluna[j]-2*m[i][j]>peça:
            peça=soma_linha[i]+soma_coluna[j]-2*m[i][j]
print(peça)            