# -*- coding: utf-8 -*-

n=int(input())
a=[]
for i in range(0,n,1):
    valor=int(input())
    a.append(valor)
    
entrada=int(input())
saida=int(input())
soma=0
i=0
for i in range (entrada,saida):
    soma = soma + a[i]
print(soma)
    
    
