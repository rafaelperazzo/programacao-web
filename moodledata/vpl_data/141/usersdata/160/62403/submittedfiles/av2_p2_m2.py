# -*- coding: utf-8 -*-

def degrau(a):
    soma=0
    for i in range(0,len(a),1):
        soma = soma + (a[i]+a[i+1])
    return(soma)
    
n=int(input('Digite o tamanho da sequência:'))
a=[]
for i in range(0,n,1):
    valor=int(input('Digite os elementos da lista:'))
    a.append(valor)
    
print(degrau(a))
