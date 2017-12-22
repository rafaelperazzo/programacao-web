# -*- coding: utf-8 -*-
#função que verifica a diagonal dominante
def diagdomini(mat):
    for w in range (0,(len(mat)-1,1) :
        if 2*(mat[w][w])>sum(mat[w]):
            return 'S'
        else:
            return 'N'
        



a= []

n=int(input('Digite a ordem da matriz: '))

for i in range (0,n,1) :
    lista = []
    for j in range (0,n,1):
        lista.append(float(input('Digite o A%d%d: ' %  ((i+1),(j+1)))))
    matriz.append(lista)
        
        
