# -*- coding: utf-8 -*-
tamanho = int(input('Digite o tamnha da matriz: '))



matriz = [ ]

for i in range(tamanho):
    linhas = [ ]
    for j in range(tamanho):
        linhas.append(int(input('Digite os elementos da linha: ')))
    matriz.append(linhas)
    

print(matriz)


dominante = False
for i in range(tamanho):
    diagonal = matriz[i][i]
    soma = sum(matriz[i]) - diagonal
    if diagonal >= soma :
        dominante = True
    else:
        dominante = False
        
if dominante == True:
    print("'SIM'")
else:
    print("'NAO'")
    
           


            
    