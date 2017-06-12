# -*- coding: utf-8 -*-
def simpares(a):
    soma=0
    for i in range (0,len(a),1):
        if a[i]%2==1:
            soma=soma+a[i]
    return (soma)
def spares(a):
    soma=0
    for i in range (0,len(a),1):
        if a[i]%2==0:
            soma=soma+a[i]
    return (soma)
def impares(a):
    cont=0
    for i in range (0,len(a),1):
        if a[i]%2==1:
            cont=cont+1
    return (cont)        
def pares(a):
    cont=0
    for i in range(0,len(a),1):
        if a[i]%2==0:
            cont=cont+1
    return (cont)

n=int(input('Digite a quantidade de números: '))
x=[]
for i in range (0,n,1):
    lista=int(input('Digite o valor: '))
    x.append(lista)
print('%.f'%simpares(x))
print('%.f'%spares(x))
print('%.f'%impares(x))
print('%.f'%pares(x))
print(x)



