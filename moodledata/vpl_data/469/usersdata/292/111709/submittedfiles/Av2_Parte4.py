# -*- coding: utf-8 -*-
################################################### -> CLASSES
class Quadras(object):
    def __init__(self, M, N):
        self.linhas = M
        self.colunas = N
        self.bairro = []
        for i in range(M):
            linha = []
            for j in range(N):
                Vq = int(input())
                while True:
                    if 1 <= Vq <= 100:
                        break
                    
                    Vq = int(input("!!! "))
                    
                linha.append(Vq)
                
            self.bairo.append(linha)
            
    def minPreço(self):
        somatPreço = []
        
        for i in self.bairro:
            somatPreço.append(sum(i))
            
        self.melhorPreço = min(somatPreço)
        
        print(self.melhorPreço)
        
################################################### -> PROGRAMA PRINCIPAL

M = int(input())
while True:
    if 2 <
N = int(input())