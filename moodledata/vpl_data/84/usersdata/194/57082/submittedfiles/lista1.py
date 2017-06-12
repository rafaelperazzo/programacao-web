# -*- coding: utf-8 -*-
def somaimpares(a):
    soma=0
    for i in range(0,len(a),1):
        if a[i]%2==1:
            soma=soma+a[i]
    return(soma)

def somapares(a):
    soma=0
    for i in range(0,len(a),1):
        if a[i]%2==0:
            soma=soma+a[i]
    return(soma)

def impares(a):
    cont=0
    for i in range(0,len(a),1):
        if a[i]%2==1:
            cont=cont+a[i]
    return(cont)
  
def pares(a):
    cont=0
    for i in range(0,len(a),1):
        if a[i]%2==0:
            cont=cont+a[i]
    return(cont)

n=int(input('digite a quantidade de números:'))
b=[]
for i in range(0,n,1):
    lista=int(input('digite o valor:'))
    b.append(lista)
    
print('%.f'%somaimpares(b))
print('%.f'%somapares(b))
print('%.f'%impares(b))
print('%.f'%pares(b))
print(b)



