# -*- coding: utf-8 -*-
n=int(input('digite um valor de elementos:'))
def somaimpar(a):
    soma=0
    for i in range(0,len(a),1):
        if a[i]%2!=0:
            soma=soma+a[i]
    return soma
    
def somapar(a):
    soma=0
    for i in range(0,len(a),1):
        if a[i]%2==0:
            soma=soma+a[i]
        return soma

def qpar(a):
    cont=0
    for i in range(0,len(a),1):
        if a[i]%2==0:
            cont=cont+1
        return cont

def qimpar(a):
    cont=0
    for i in range(0,len(a),1):
        if a[i]%2!=0:
            cont=cont+1
        return cont

lista=[]
for i in range(0,len(lista),1):
    elemento=int(input('digite um elemento:'))
        
print(somaimpar(lista))
print(somapar(lista))
print(qimpar(lista))
print(qpar(lista))
print(lista)













