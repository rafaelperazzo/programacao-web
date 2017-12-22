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
            
    def pqM(self):
        Matriz.transposta(self)
        
        somas_l, somas_c, somas = [], [], []
        
        for i in self.matriz:
            somas_l.append(sum(i))
            somas.append(sum(i))
            del i
            
        for i in self.transposta:
            somas_c.append(sum(i))
            somas.append(sum(i))
            del i
            
        for i in somas:
            cont = 0
            for j in somas:
                if i == j:
                    cont += 1
                    
                del j
            if cont == (2*self.dim - 2):
                val_ref = i
                del i
                break
        
        for i in range(0, len(somas_l)):
            if somas_l[i] != val_ref:
                ind_i = i
                del i
                break
            
        for i in range(0, len(somas_c)):
            if somas_c[i] != val_ref:
                ind_j = i
                del i
                break
            
        colocou_no_lugar = self.matriz[ind_i][ind_j]
        
        original = val_ref - (sum(self.matriz[ind_i]) - colocou_no_lugar)
        
        print(original)
        print(colocou_no_lugar)
                
    def mostraMatriz(self):
        for i in self.matriz:
            print(i)
            del i
        
        print("\n")
        
        Matriz.transposta(self)
        for i in self.transposta:
            print(i)
            del i
            
#################################### - PROGRAMA PRINCIPAL - ###########################################
N = int(input())
A = Matriz(N)
A.mostraMatriz()
A.pqM()
