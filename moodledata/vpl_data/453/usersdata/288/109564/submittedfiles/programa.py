# -*- coding: utf-8 -*-
n=int(input("Digite a ordem da matriz:"))
m=[' ']
peso=0
for i in range (0,n,1):
    l=[' ']
    for j in range (0,n,1):
        l.append (int(input("Digite um numero para a matriz:")))
    m.append (l)
    
    soma_linha=0
    soma_coluna=0
    for k in range (0,n,1):
        soma_linha = sum (m[i][k])
        soma_coluna = sum (m[k][j])
    soma_total= soma_linha + soma_coluna - 2*m[i][j]
    if soma_total>peso:
        peso=soma_total
print (peso)
    
