# -*- coding: utf-8 -*-
def somapares(a):
    soma=0
    for i in range(0,len(a),1):
        if a[i]%2==0:
            soma=soma+a[i]
    return(soma)
n=int(input('Digite quantidade de elementos: '))
for i in range(0,n,1):
    valor=int(input('Digite um elemento: '))
    a.append(valor)
print(somapares(a))

def somaimpares(a):
    soma=0
    for i in range(0,len(a),1):
        if a[i]%2==1:
            soma=soma+a[i]
    return(soma)
n=int(input('Digite quantidade de elementos: '))
for i in range(0,n,1):
    valor=int(input('Digite um elemento: '))
    a.append(valor)
print(somaimpares(a))


def cimpares(a):
    cont=0
    for i in range(0,len(a),1):
        if a[i]%2==1:
            cont=cont+1
    return(cont)
n=int(input('Digite quantidade de elementos: '))
for i in range(0,n,1):
    valor=int(input('Digite um elemento: '))
    a.append(valor)
print(cimpares(a))

def cpares(a):
    cont=0
    for i in range(0,len(a),1):
        if a[i]%2==0:
            cont=cont+1
    return(cont)
n=int(input('Digite quantidade de elementos: '))
for i in range(0,n,1):
    valor=(input('Digite um elemento: '))
    a.append(valor)
print(cpares(a))