import numpy as np

dimensao = int (input('Digite a dimensao da matriz:'))
indice_linha = int (input('Digite a linha:'))
indice_coluna = int (input('Digite a coluna:'))
a = np.zeros ((dimensao,dimensao))

for i in range (0,dimensao,1):
  for j in range (0,dimensao,1):
    a[i,j] = int (input('Digite o elemento da matriz:'))

def somalinha (matriz,indice_linha):
  soma = 0
  for j in range (0,matriz.shape[1],1):
    soma = soma + matriz[indice_linha,j]
    return soma
    
def somacoluna (matriz,indice_coluna):
  soma = 0
  for i in range (0,matriz.shape[0],1):
    soma = soma + matriz [i,indice_coluna]
    return soma
    
print (somalinha(a,indice_linha) + somacoluna(a,indice_coluna)- (2*a[indice_linha,indice_coluna]))
  
    

