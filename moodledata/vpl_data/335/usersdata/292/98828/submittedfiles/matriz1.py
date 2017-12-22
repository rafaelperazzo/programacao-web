# -*- coding: utf-8 -*-
class Matriz(object):
    def __init__(self, m, n):
        self.linhas = m
        self.colunas = n
        self.matriz = []
        for i in range(1, m+1):
            linhas = []
            for j in range(1, n+1):
                linhas.append(int(input("Digite o elemento a%d%d da matriz: "%(i,j))))
            self.matriz.append(linhas)
            
    def mostraMatriz(self):
        for i in self.matriz:
            print(i)
            
    def corteRetangularBinario(self):
        cont = 0
        for linha in self.matriz:
            for elmt in linha:
                if (elmt != 0) and (elmt != 1):
                    cont +=1
        if cont == 0:
            print("É possível!")
        
        else:
            print("Não é possível realizar o corte Binário!")
            
################################ - PROGRAMA PRINCIPAL - ################################
m = int(input("Digite o número de linhas: "))
n = int(input("Digite o número de colunas: "))
A = Matriz(m, n)
A.mostraMatriz()
A.corteRetangularBinario()