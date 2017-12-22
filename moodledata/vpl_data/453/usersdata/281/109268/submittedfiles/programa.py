# -*- coding: utf-8 -*-
m=[]
n=int(input('Digite a dimensão do tabuleiro: '))
for j in range (0,n,1):
    m.append(int(input('Digite o números %d de entrada: '% (j+1))))    
    for i in range (0,n,1):
        m.append(int(input('Digite o números %d de entrada: '% (i+1))))
print(m)    
