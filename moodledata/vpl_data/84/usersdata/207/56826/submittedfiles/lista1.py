# -*- coding: utf-8 -*-
def somatorio1(a):
    soma=0
    for i in range(0,len(a),1):
        if a [i]%2==1:
             soma=soma+a[i]
    return(soma)
    
def somatorio2(a):
    soma=0
    for i in range(0,len(a),1):
        if a [i]%2==0:
             soma=soma+a[i]
    return(soma)
    
def quantidade1(a):
    cont=0
    for i in range(0,len(a),1):
        if a [i]%2==0:
             cont=cont+1
    return(soma)

def somatorio2(a):
    cont=0
    for i in range(0,len(a),1):
        if a [i]%2==0:
             cont=cont+1
    return(cont)
    
n=int(input('escreva o valor do n:'))
x=[]
for i in range(1,n+1,1):
    lista=int(input('escreva o valor da lista:'))
    x.append(lista)
print('%.f'%somatorio1(x))
print('%.f'%somatorio2(x))
print('%.f'%quantidade1(x))
print('%.f'%quantidade2(x))
print(x)
    