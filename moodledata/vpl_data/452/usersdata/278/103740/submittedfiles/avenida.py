# -*- coding: utf-8 -*-
m = int(input('Digite o número de quadras no sentido Norte-Sul: '))
while (m<2 or m>1000):
    m = int(input('Digite o número de quadras [2,1000] no sentido Norte-Sul: '))
n = int(input('digite o número de quadras no sentido Leste-Oeste: '))
while (n<2 or n>1000):
    n = int(input('digite o número de quadras [2,1000] no sentido Leste-Oeste: '))
valor = []
for i in range (0,m,1):
    for j in range (0,n,1):
        valor.append(int(input('Digite o valor de desapropriação da quadra%d%d: ' %(i+1,j+1))))
soma=0
valor2=[]
for j in range (0,n,1):
    for i in range (0,m,1):
        soma+=valor[i][j]
    valor2.append(soma)
while ((len soma)>1):
    for i in range (0,n,1):
        if (i+1)<n:
            if soma[i]<soma[i+1]:
                del soma[i+1]
print(soma[0])
        
            
            

