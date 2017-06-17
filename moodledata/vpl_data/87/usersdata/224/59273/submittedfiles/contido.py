# -*- coding: utf-8 -*-
def iguais(a,b):
    cont=0
    for i in range(0,len(a),1):
        if a[i] in b:
            cont=cont+1
    return cont
    
n=int(input('Digite a quantidade de elementos de a: ')) 
a=[]
for i in range(1,n+1,1):
    valor=int(input('a: '))
    a.append(valor)
m=int(input('Digite a quantidade de elementos de b: '))
b=[]
for i in range(1,m+1,1):
    y=int(input('b: '))
    b.append(y)
print(iguais(a,b))