# -*- coding: utf-8 -*-
N = int(input('Digite a dimensão do tabuleiro quadrado: '))
while (N<3):
    N = int(input('Digite a dimensão (N>=3) do tabuleiro quadrado: '))
m=[]
for i in range (0,N,1):
    lista=[]
    for j in range (0,N,1):
        lista.append(int(input('Digite o número da linha%.d e coluna%.d: ' %(i,j))))
    m.append(lista)
    
        