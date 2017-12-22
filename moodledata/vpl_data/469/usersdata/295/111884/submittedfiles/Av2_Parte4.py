# -*- coding: utf-8 -*-
import math
matriz=[]
m = int(input("Digite o numero de quadras no sentindo N-S: "))
while m<=2 and m>=1000:
    m = int(input("Digite o numero de quadras no sentindo N-S: "))
n = int(input("Digite o numero de quadras no sentindo L-O: "))
while n<=2 and n>=1000:
    n = int(input("Digite o numero de quadras no sentindo L-O: "))
    
for i in range(0,m,1):
    linhas=[]
    for j in range(0,n,1):
        linhas.append(int(input("Digite o valor:")))
    matriz.append(linhas)
        

i=0
somatorio = sum(matriz[i]) + sum(matriz[i+1])      
if sum(matriz[i]) + sum(matriz[i+1]) <= 100:
    print(somatorio)
