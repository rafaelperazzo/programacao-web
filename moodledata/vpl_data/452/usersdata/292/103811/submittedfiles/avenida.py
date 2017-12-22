# -*- coding: utf-8 -*-
class Quadras(object):
    def __init__(self, M, N):
        self.norte_sul = M
        self.leste_oeste = N
        self.quadras = []
        
        for i in range(1, M+1):
            linhas = []
            for j in range(1, N+1):
                q = int(input())
                
                while True:
                    if 1 <= q <= 100:
                        break
                    q = int(input())
                
                linhas.append(q)
            self.quadras.append(linhas)
            
    def mostraQuadras(self):
        print("\n")
        for i in self.quadras:
            print(i)
            
    def minimizaPreco(self):
        preços= []
        for i in self.quadras:
            preços.append(sum(i))
            
        for i in range(0, self.leste_oeste):
            soma_colunas = 0
            
            for j in range(0, self.norte_sul):
                soma_colunas += self.quadras[j][i]
                
            preços.append(soma_colunas)
            
        self.preco_minimizado = min(preços)
        print(self.preco_minimizado)
            
            
##################################################################### - PROGRAMA PRINCIPAL - ###############################################################################################################

M = int(input())
while True:
    if 2 <= M <= 1000:
        break
    M = int(input())

N = int(input())
while True:
    if 2 <= N <= 1000:
        break
    N = int(input())
    
Q = Quadras(M, N)
Q.minimizaPreco()
