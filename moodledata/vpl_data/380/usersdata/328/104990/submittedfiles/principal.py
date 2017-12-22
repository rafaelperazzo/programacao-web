m = input('Digite a quantidade de linhas: ')

matriz = []

matriz.append([50,70,20])

n = len(matriz[0])

for i in range(1,m+1,1):

    linha = []

    for j in range(0,n,1):

        linha.append(input('Digite um valor: '))

    matriz.append(linha)