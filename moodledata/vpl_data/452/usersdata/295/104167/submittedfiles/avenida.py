# -*- coding: utf-8 -*-
matriz = []
m = int(input("Digite um numero de quadras n-s:"))
while m > 1000 or m < 2:
    m = int(input("Digite um numero de quadras n-s:"))
n = int(input("Digite um numero de quadras l-s:"))    
while n > 1000 or n < 2:
    n = int(input("Digite um numero de quadras l-s:")) 

for i in range(0,m,1):
    linha = []
    for j in range(0,n,1):
        linha.append(int(input("Digite um valor para a quadra: ")))
    matriz.append(linha)
print(matriz)

               
                

                
    