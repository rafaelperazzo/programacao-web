# -*- coding: utf-8 -*-
tamanho = int(input('Digite o tamnha da matriz: '))



matriz = [ ]

for i in range(tamanho):
    linhas = [ ]
    for j in range(tamanho):
        linhas.append(int(input('Digite os elementos da linha: ')))
    matriz.append(linhas)
    

print(matriz)


primeiro = matriz[0][0]
for i in range(tamanho):
    diagonal=sum(matriz[i][i])-primeiro
    if primeiro>=diagonal:
        primeiro=True
    else:
        primeiro=False
        
'''
dominante = False
for i in range(tamanho):
    soma = 0
    for j in range(tamanho)
        if i != j
            soma = soma + matriz[i][j]
'''
           
if primeiro==True:
    print('''SIM''')
else:
    print('''NAO''')
    
           


            
    