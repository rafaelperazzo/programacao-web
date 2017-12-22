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
for i in range(n):
    soma = 0
    for j in range(n):
        soma += matriz[j][i]
    for l in range(n):
        soma = 0
        soma += soma + sum(matriz[l])
        if soma > maior:
            maior  = soma
print(maior)
    
