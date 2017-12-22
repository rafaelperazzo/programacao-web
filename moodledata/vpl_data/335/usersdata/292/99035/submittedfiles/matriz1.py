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
        cont_ver, cont_zeros = 0, 0
        for linha in self.matriz:
            for elmt in linha:
                if (elmt != 0) and (elmt != 1):
                    cont_ver +=1
                    
                if (elmt == 0):
                    cont_zeros +=1
                    
        if (cont_ver != 0) or (cont_zeros == (self.linhas*self.colunas)):
            print("Não é possível realizar o corte Binário!")
        
        else:
            cont_1_sup, cont_1_sup_aux = 0, 0
            cont_1_inf, cont_1_inf_aux = self.linhas-1, self.linhas-1
            cont_1_r, cont_1_l = -1, -1
            for linha in self.matriz:
                if 1 in linha:
                    cont_1_sup = cont_1_sup_aux
                    break
                cont_1_sup_aux += 1
            
            self.matriz.reverse()
            for linha in self.matriz:
                if 1 in linha:
                    cont_1_inf = cont_1_inf_aux
                    break
                cont_1_inf_aux -= 1
            self.matriz.reverse()
            
            for i in range(0, self.colunas):
                for j in range(0, self.linhas):
                    if self.matriz[i][j] == 1:
                        cont_1_r = i
                        break
                if cont_1_r == i:
                    break
                
            for i in range(self.colunas-1, -1, -1):
                for j in range(self.linhas-1, -1, -1):
                    if self.matriz[i][j] == 1:
                        cont_1_l = i
                        break
                if cont_1_l == i:
                    break
                
            
            matrizCortada = []
            for i in range(cont_1_sup, cont_1_inf+1):
                linhas_matrizCortada = []
                
                for j in range(cont_1_r, cont_1_l+1):
                    linhas_matrizCortada.append(self.matriz[i][j])
                    
                matrizCortada.append(linhas_matrizCortada)
                
            #E Finalmente...
            print(matrizCortada)
            
            
################################ - PROGRAMA PRINCIPAL - ################################
m = int(input("Digite o número de linhas: "))
n = int(input("Digite o número de colunas: "))
A = Matriz(m, n)
A.mostraMatriz()
A.corteRetangularBinario()