# -*- coding: utf-8 -*-
tamanho = int(input('Digite o tamnha da matriz: '))



matriz=[]

for i in range(tamanho):
    linhas=[]
    for j in range(tamanho):
        linhas.append(int(input('Digite os elementos da linha: ')))
    matriz.append(linhas)
    

print(matriz)


primeiro=matriz[0][0]
for i in range(tamanho):
    if primeiro>=sum(int(matriz[i][i]))-primeiro:
        primeiro=True
    else:
        primeiro=False
        
           
           
if primeiro==True:
    print('''SIM''')
else:
    print('''NAO''')
    
           


            
    