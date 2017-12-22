# -*- coding: utf-8 -*-
class MatrizQuad(object):
    def __init__(self, dim):
        self.dim = dim
        self.matriz = []
        for i in range(1, dim+1):
            linhas = []
            for j in range(1, dim+1):
                linhas.append(int(input("Digite o elemento a%d%d da matriz: "%(dim, dim))))
            self.matriz.append(linhas)
            
    def diagonalDominante(self):
        cont = 0
        for i in range(0, self.dim):
            if self.matriz[i][i] > (sum(self.matriz[i]) - self.matriz[i][i]):
                cont += 1
                
        if cont == self.dim:
            print("SIM")
            
        else:
            print("NAO")
            
#################################### - PROGRAMA PRINCIPAL - ####################################
n = int(input("Digite a ordem da matriz: "))
A = MatrizQuad(n)
A.diagonalDominante()
            
        
