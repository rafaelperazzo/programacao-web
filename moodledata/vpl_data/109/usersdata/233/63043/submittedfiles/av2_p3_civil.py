# -*- coding: utf-8 -*-
n=int(input('n: '))
matriz=np.zeros((n,n))
somacolunas=0
for j in range(matriz.shape[1]):
    somacolunas=somacolunas+matriz[a,j]
somalinhas=0
for i in range(matriz.shape[0]):
    somalinhas=somalinhas+matriz[i,b]
somatotal=somalinhas+somacolunas-2*matriz[a,b]
print(somatotal)

