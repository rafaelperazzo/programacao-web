# -*- coding: utf-8 -*-
n = 0
matriz = [] 
m = int(input("Digite sua idade: "))
    while m<18:
        m = int(input("Digite sua idade: "))
       

n = int(input("Digite sua altura: "))
    while n<0:
        n = int(input("Digite sua altura: "))
    
for i in range(1,n+100):
    linha=[]
    for i in range(1,n+100):
        x = int(input("Digite o valor da idade"))
        linha.append(x)
        
    matriz.append(linha)