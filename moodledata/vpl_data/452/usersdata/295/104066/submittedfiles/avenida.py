# -*- coding: utf-8 -*-
matriz = []
m = int(input("Digite um numero de quadras n-s:"))
while m > 1000 or m < 0:
    m = int(input("Digite um numero de quadras n-s:"))
n = int(input("Digite um numero de quadras l-s:"))    
while 0<= i <=m-1:
    n = int(input("Digite um numero de quadras l-s:")) 
i = 0
j = 0
if 2<= n <=1000:
    if 0<= j <=n-1:
        for i in range(0,m,1):
            linha = []
            for j in range(0,n,1):
                linha.append(int(input("Digite um valor para a quadra: ")))
                matriz.append(linha)
print(matriz)
               
                

                
    