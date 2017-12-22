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
        valor1.append(int(input('Digite o valor de desapropriação da quadra%d%d: ' %(i,j))))
    valor2.append(valor1)
soma=0
valor=[]
for j in range (0,n,1):
    for i in range (0,m,1):
        soma=soma+valor2[i][j]
    valor.append(soma)
a=0
while (n>1):
    if a+1<n:
        if valor[a]<valor[a+1]:
            del valor[a+1]
        else:
            del valor[a]
print(valor[0])
            
            

