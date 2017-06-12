# -*- coding: utf-8 -*-
def simpares(a):
    soma=0
    for i in range(0,len(a),1):
        if a[i]%2==1:
            soma=soma+a[i]
    return(soma)

def spares(a):
    soma=0
    for i in range(0,len(a),1):
        if a[i]%2==0:
            soma=soma+a[i]
    return(soma)

def qimpares(a):
    cont=0
    for i in range(0,len(a),1):
        if a[i]%2==1:
            cont=cont+1
    return(cont)
    
def qpares(a):
    cont=0
    for i in range(0,len(a),1):
        if a[i]%2==0:
            cont=cont+1
    return(cont)

n=int(input('Digite a Quantidade de Elementos da Lista:'))
l1=[]
for i in range(0,n,1):
    v=int(input('Digite um Valor para a Lista:'))
    l1.append(v)

print('%.f' %simpares(l1))
print('%.f' %spares(l1))
print('%.f' %qimpares(l1))
print('&.f' %qpares(l1))
print(l1)

