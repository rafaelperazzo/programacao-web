from __future__ import division

m = int(input('Digite o número de linhas'))
n = int(input('Digite o número de colunas'))
matriz = []
for i in range (0,m,1):
    vetor = []
    for j in range (0,n,1):
        x = int(input('Digite o termo %d%d'(i,j)))
        vetor.append(x)
matriz.append(vetor)

#programa_matriz_simétrica
cont = 0
meio = n//2
y = n -1
for x in range (0,m,1):
    if (matriz[:,x]!=matriz[:,y]):
        cont = cont+1
        y = y-1
if cont == 0:
    print ('É simétrica')
else:
    print ('Não é simétrica')
