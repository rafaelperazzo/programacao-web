# -*- coding: utf-8 -*-
class Tabuleiro(object):
    def __init__(self, N):
        self.dim = N
        self.tab = []
        for i in range(1, N+1):
            linha = []
            for j in range(1, N+1):
                linha.append(int(input("Digite o número da casa (%d, %d): "%(i, j))))
                
                del j
            self.tab.append(linha)
            
            del i, linha
            
    def pesoMaximo(self):
        pesos = []
        for i in range(0, self.dim):
            for j in range(0, self.dim):
                soma_l, soma_c = 0, 0
                for k in range(0, self.dim):
                    soma_l += self.tab[i][k]
                    soma_c += self.tab[k][j]
                    
                    del k
                soma_l -= self.tab[i][j]
                soma_c -= self.tab[i][j]
                pesos.append(soma_l+soma_c)
                
                del j
            
            del i, soma_c, soma_l
            
        print(max(pesos))
    
    def mostraTabuleiro(self):
        for i in self.tab:
            print(i)
            
            del i
            
########################################## - PROGRAMA PRINCIPAL - ############################
N = int(input("Digite a dimensão do Tabuleiro: "))
while True:
    if N >= 3:
        break
    
    N = int(input("Valor inválido! Digite novamente: "))
    
tab = Tabuleiro(N)
tab.mostraTabuleiro()
tab.pesoMaximo()