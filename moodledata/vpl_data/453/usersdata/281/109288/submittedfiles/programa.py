# -*- coding: utf-8 -*-
m=[]
n=int(input('Digite a dimensão do tabuleiro: '))
x=n*n
for i in range (0,x,1):
    m.append(int(input('Digite o números %d de entrada: '% (i+1))))
print(m)    
