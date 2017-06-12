# -*- coding: utf-8 -*-
def somaimpar(a):
    soma=0
    for i in range (0,len(a),1):
        if a[i]%2!=0:
            soma=soma+a[i]
    return soma

def somapar(a):
    soma=0
    for i in range (0,len(a),1):
        if a[i]%2==0:
            soma=soma+a[i]
    return soma
    
def qimpar(lista):
    cont=0
    for i in range (0,len(lista),1):
        if i%2!=0:
            cont=cont+1
    return cont

def qpar(lista):
    cont=0
    for i in range (0,len(lista),1):
        if i%2==0:
            cont=cont+1
    return cont

h=[ ]
n=int(input('Digite o número de elementos da lista: '))
for i in range (1,n+1,1):
    a=int(input('Digite o valor do elemento da lista: '))
    h.append(a)

print(somaimpar(h))
print(somapar(h))
print(qimpar(h))
print(qpar(h))

