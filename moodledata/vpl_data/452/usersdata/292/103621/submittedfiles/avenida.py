# -*- coding: utf-8 -*-
class Quadras(object):
    def __init__(self, M, N):
        self.norte_sul = M
        self.leste_oeste = N
        self.quadras = []
        
        for i in range(1, M+1):
            linhas = []
            for j in range(1, N+1):
                q = float(input("Digite o valor (em milhões de reais) da %dº quadra no sentido Norte-sul que também é a %dº no sentido Leste-oeste: "%(i,j)))
                
                while True:
                    if 1 <= q <= 100:
                        break
                    q = float(input("Valor fora da faixa! Digite novamente: "))
                
                linhas.append(q)
            self.quadras.append(linhas)
            
    def mostraQuadras(self):
        print("\n")
        for i in self.quadras:
            print(i)
        
            
####################################################################################################################################################################################

M = int(input("Digite o número de casas do sentido Norte-sul: "))
N = int(input("Digite o número de casas do sentido Leste-oeste: "))
Q = Quadras(M, N)
Q.mostraQuadras()