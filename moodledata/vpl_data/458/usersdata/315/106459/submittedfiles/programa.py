# -*- coding: utf-8 -*-

#ENTRADA LINHASXCOLUNA ---------------------------------------------------------------------
while True:
    m = int(input('Digite quant linhas: '))
    if m>=2:
        break

while True:
    n = int(input('Digite quant colunas: '))
    if n>=2:
        break
#--------------------------------------------------------------------------------------------

#MATRIZ PRINCIPAL
matriz = []
for i in range(m):
    v = []
    for j in range(n):
        v.append(int(input('Digite valor: ')))
    matriz.append(v)
    
    
#MATRIZ TRANSPOSTA
mt = []
for i in range (n):
    v = []
    for j in range (m):
        v.append( matriz[j][i] )
    mt.append(v)
    
print(matriz[0])
print(matriz[1])
print(matriz[2])
print(mt[0])
print(mt[1])
print(mt[2])










