import numpy as np

dimensao = int (input('Digite a dimensao da matriz:'))
x = int (input('Digite a linha:'))
y = int (input('Digite a coluna:'))
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
    
resultado = somalinha(a,x) + somacoluna(a,y)- (2*a[x,y])
print ('%d' %resultado)
  
    

