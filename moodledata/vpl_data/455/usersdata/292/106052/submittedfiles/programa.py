# -*- coding: utf-8 -*-
class Matriz(object):
    def __init__(self, N):
        self.dim = N
        del N
        self.matriz = []
        for i in range(1, self.dim+1):
            linha = []
            for j in range(1, self.dim+1):
                linha.append(int(input()))
                del j
            self.matriz.append(linha)
            del i
            
    def transposta(self):
        self.transposta = []
        for i in range(0, self.dim):
            linha = []
            for j in range(0, self.dim):
                linha.append(self.matriz[j][i])
                
                del j
                
            self.transposta.append(linha)
            del i
            
    def mostraMatriz(self):
        for i in self.matriz:
            print(i)
            del i
        
        print("\n")
        
        Matriz.transposta()
        for i in self.transposta:
            print(i)
            del i
            
#################################### - PROGRAMA PRINCIPAL - ###########################################
N = int(input())
A = Matriz(N)
A.mostraMatriz()

