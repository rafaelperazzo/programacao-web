# -*- coding: utf-8 -*-
def somadosimpares(a):
    soma=0
    for i in range(0,len(a),1):
        if a[i]%2==1:
            soma=soma+a[i]
    return(soma)

def somadospares(b):
    soma=0
    for i in range(0,len(b),1):
        if b[i]%2==0:
            soma=soma+b[i]
    return(soma)
    
def impares(c):
    cont=0
    for i in range(0,len(c),1):
        if c[i]%2==1:
            cont=cont+1
    return(cont)
    
def pares(d):
    cont=0
    for i in range(0,len(d),1):
        if d[i]%2==0:
            cont=cont+1
    return(cont)
    
n=int(input('digite a quantidade:'))
g=[]
for i in range(0,n,1):
    lista=int(input('digite o número:'))
    g.append(lista)

print('%.f'%somadosimpares(g))
print('%.f'%somadospares(g))
print('%.f'%impares(g))
print('%.f'%pares(g))
print(g)


