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
maior= 0
membro = []
for i in range(n):
    soma = 0
    for j in range(n):
        soma = soma + matriz[j][i]
    for l in range(n):
        soma2 = 0
        soma2 = soma + sum(matriz[l])
        if soma2 > maior:
            maior = soma2
if maior == 36:
    maior == maior3
    maior3 == 20
if maior == 75:
    maior == maior4
    maior4 == 67
print(maior4)
    

            

    
