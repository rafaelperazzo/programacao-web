# -*- coding: utf-8 -*-
def cria_matriz_quadra(n):
    matriz=[]
    for i in range (n):
        linha = []
        for j in range (n):
            for i in range (0,n-1,1):
                valor_inicial=int(input(linha.append("digite o valor: ")))
        matriz.append(linha)
    return matriz


def main():
    n=int(input("digite a dimensão para linhas e calunas:"))
    matriz = cria_matriz_quadra(n,1)
    print(matriz)
    return

main()



