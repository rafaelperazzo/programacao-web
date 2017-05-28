# -*- coding: utf-8 -*-
def impares(a):
    soma=0
    for i in range (0,len(a),1):
        if a[i]%2!=0:
            soma=soma+a[i]
    return soma
  
def pares(a):
    soma=0
    for i in range (0,len(a),1):
        if a[i]%2==0:
            soma=soma+a[i]
    return soma
    
def quantimpares(a):
    soma=0
    for i in range (0,len(a),1):
        if a[i]%2!=0:
            soma=soma+1
    return soma    

def quantpares(a):
    soma=0
    for i in range (0,len(a),1):
        if a[i]%2==0:
            soma=soma+1
    return soma
    
lista=[ ]
n=int(input('Digite a quantidade de elementos da lista:'))
for i in range (0,n,1):
    valor=float(input('Digite o valor:'))
    lista.append(valor)

print impares(lista)
print pares(lista)
print quantimpares(lista)
print quantpares(lista)
    
    