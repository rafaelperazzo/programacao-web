# -*- coding: utf-8 -*-
n = 0
matriz = [] 
m = int(input("Digite sua idade: "))
while m<18:
    m = int(input("Digite sua idade: "))
       

n = int(input("Digite sua altura: "))
while n<0:
    n = int(input("Digite sua altura: "))
    
for i in range(1,n+6):
    linha=[]
    for i in range(1,n+6):
        x = int(input("Digite sua idade:"))
        y = int(input("Digite sua altura: "))
        linha.append(x)
        linha.append(y)
          
    matriz.append(linha)

media_altura = sum(n)/len(n)
print(media_altura)