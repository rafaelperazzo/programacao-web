# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
# 1) Vamos pedir as dimensões da matriz

m = int(input('Digite a quantidade de linhas: '))

n = int(input('Digite a quantidade de colunas: '))

# 2) Vamos criar a matriz vazia

a = []

# 3) Vamos pedir os números e popular toda a matriz

for i in range(0,m,1):

    l = []

    for j in range(0,n,1):

        l.append(float(input('Digite o numero: ')))

    a.append(l)

# 4) Vamos procurar o maior valor

maior = a[0][0]

for i in range(0,m,1):

    for j in range(0,n,1):

        if a[i][j] > maior:

            maior = a[i][j]

# 5) Vamos mostrar o maior

print(maior)