# -*- coding: utf-8 -*-
while(True):
    n = int(input("Digite a dimensão do tabuleiro: "))
    if n>=3:
        break
    else:
        print('dimensão inválida')
matriz = []
for i in range(n):
    linha = []
    for j in range(n):
        linha.append(int(input("Digite o elemento %d de %d: " %((j+1),(i+1)))))
    matriz.append(linha)
maior = 0
maior2 =0
for i in range(n):
    soma = 0
    for j in range(n):
        soma += matriz[j][i]
    for l in range(n):
        soma2 = 0
        soma2 = soma + sum(matriz[l])-matriz[i][l]
        if soma2 > maior2:
            maior2  = soma2
    if maior2 > maior:
        maior = maior2
print(maior)
    
