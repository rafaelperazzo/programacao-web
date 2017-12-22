import numpy as np

m = int (input('Digite a dimensao da matriz:'))
linha = int (input('Digite a linha:'))
coluna = int (input('Digite a coluna:'))
a = np.zeros ((m,m))

for i in range (0,m,1):
  for j in range (0,m,1):
    a[i,j] = int (input('Digite o elemento da matriz:'))

def somalinha (matriz,linha_i):
    soma = 0
    for j in range (0,matriz.shape[1],1):
        soma = soma + matriz[linha_i,j]
    return soma
    
def somacoluna (matriz,coluna_i):
    soma = 0
    for i in range (0,matriz.shape[0],1):
        soma = soma + matriz [i,coluna_i]
    return soma
    
resultado = somalinha(a,linha) + somacoluna(a,coluna)- (2*a[linha,coluna])
print ('%d' %resultado)
  
    

