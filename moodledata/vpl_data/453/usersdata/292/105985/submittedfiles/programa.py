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