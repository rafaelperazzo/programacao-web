# -*- coding: utf-8 -*-
def cria_matriz_quadra(n,valor_inicial):
    matriz=[]
    for i in range (n):
        linha = []
        for j in range (n):
            linha.append(valor_inicial)
        matriz.append(linha)
    return matriz


def main():
    n=int(input("digite a dimensão para linhas e calunas:"))
    matriz = cria_matriz_quadra(n,1)
    print(matriz)
    return

main()



