# -*- coding: utf-8 -*-
n=int(input('Digite quantidade de salas:'))
pe=int(input('Digite porta de entrada:'))
ps=int(input('Digite porta de saida:'))
a=[]
for i in range(0,n,1):
    valor=int(input('Digite vida da sala:'))
    a.append(valor)
soma=0
for i in range(0,len(a)+1,1):
    soma=soma+a[i]
print(soma)
    
    
