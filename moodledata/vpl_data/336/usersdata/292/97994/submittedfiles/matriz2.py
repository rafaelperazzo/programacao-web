# -*- coding: utf-8 -*-

class MatrizQuad(object):
    def __init__(self, dim):
        self.dim = dim
        self.matriz = []
        for i in range(1, dim+1):
            linhas = []
            for j in range(1, dim+1):
                linhas.append(int(input("Digite o elemento a%d%d da matriz: "%(i,j))))
            self.matriz.append(linhas)
            
    def quadradoMágico(self):
        ref = sum(self.matriz[0])
        cont = 0
        soma_diagonal_p, soma_diagonal_s = 0, 0
        for i in range(0, self.dim):
            soma_linha, soma_coluna = 0, 0
            soma_diagonal_p += self.matriz[i][i]
            soma_diagonal_s += self.matriz[i][self.dim - i]
            
            for j in range(0, self.dim):
                soma_linha += self.matriz[i][j]
                soma_coluna += self.matriz[j][i]
            
            if (soma_linha == ref) and (soma_coluna == ref):
                cont += 2
                
        if (soma_diagonal_p == ref) and (soma_diagonal_s == ref):
            cont += 2
            
        if (cont == (self.dim*2 + 2)):
            return "S"
            
        else:
            return "N"
            
##################################################################################

n = int(input("Digite o número de linhas e colunas que queres em tua matriz: "))
A = MatrizQuad(n)
A.quadradoMágico()