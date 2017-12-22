# -*- coding: utf-8 -*-
m = int(input('Digite o número de quadras no sentido Norte-Sul: '))
while (m<2 or m>1000):
    m = int(input('Digite o número de quadras [2,1000] no sentido Norte-Sul: '))
n = int(input('digite o número de quadras no sentido Leste-Oeste: '))
while (n<2 or n>1000):
    n = int(input('digite o número de quadras [2,1000] no sentido Leste-Oeste: '))
valor1 = []
valor2 = []
for i in range (0,m,1):
    for j in range (0,n,1):
        valor1.append(int(input('Digite o valor de desapropriação da quadra%d%d: ' %(i+1,j+1))))
    valor2.append(valor1)
soma=0
valor3=[]
for j in range (0,n,1):
    for i in range (0,m,1):
        soma=soma+valor2[i][j]
    valor3.append(soma)
for i in range (0,n,1):
    if i<n:
        if valor3[i]<valor3[i+1]:
            del valor3[i+1]
        else: 
            del valor3[i]
    else:
        print(valor3[0])
        
            
            

