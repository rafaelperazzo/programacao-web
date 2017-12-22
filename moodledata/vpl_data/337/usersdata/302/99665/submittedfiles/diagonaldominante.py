# -*- coding: utf-8 -*-
n = int(input('Digite a ordem da matriz quadrada: '))
matriz = []
for i in range(n):
    linha = []
    for j in range(n):
        linha.append(float(input('Digite o elemento %d de %d: ' %((j+1),(i+1)))))
    matriz.append(linha)
cont = 0
for i in range(n):
        if matriz[i][i] > sum(matriz[i]) - matriz[i][i]:
            cont = cont +1
if cont == n:
    print('S')
else:
    print('N')
                
        

