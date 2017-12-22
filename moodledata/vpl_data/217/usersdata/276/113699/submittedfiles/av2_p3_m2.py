import numpy as np

n = int (input ('Digite a dimensão do quadrado mágico: '))

while n<3:
    n = int (input('Digite a dimensão do quadrado mágico: '))

matriz = np.zeros ((n,n))
for i in range (0,n,1):
    for j in range (0,n,1):
        matriz[i,j] = int (input ('Digite os elementos do quadrado mágico: '))

somalinha = 0
somacoluna = 0

a = []
b = []

for i in range (0,matriz.shape[0],1):
  for j in range (0,matriz.shape[1],1):
    somalinha = somalinha + matriz[i,j]
  a.append (somalinha)
  somalinha = 0

print (a)

for j in range (0,matriz.shape[1],1):
  for i in range (0,matriz.shape[0],1):
    somacoluna = somacoluna + matriz[i,j]
  b.append (somacoluna)
  somacoluna = 0   

print (b)

def diferente (a):
    for i in range (1,len (a)-1,1):
        if a[0] != a[i]:
            if a[0] == a[i+1]:
                return a[i]
            else:
                return a[0]

diferentelinha = diferente (a)
indicelinha = a.index(diferentelinha)
print (diferentelinha)
print (indicelinha)
diferentecoluna = diferente (b)
print (diferentecoluna)
print (indicoluna)
indicecoluna = a.index(diferentelinha)

if indicelinha != 0:
  subtracao1 = a[0]-diferentelinha
  
else:
  subtracao1 = a[1]-a[0]

'''
if indicecoluna !=0:
  subtracao2 = b[0]-difentecoluna
  
else:
  sutracao2 = b[1]-b[0]
  somalinha = 0
'''

reposta = matriz [indicelinha,indicecoluna] - subtracao1

print (resposta)

