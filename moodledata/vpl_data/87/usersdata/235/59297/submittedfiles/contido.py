# -*- coding: utf-8 -*-
def iguais(lista):
    cont=0
    for i in range(0,len(lista),1):
        if lista[i]==lista[i]:
            cont=cont+1
    return (cont)




a=[]
b=[]
n=int(input('quantidade de elementos de a:'))
m=int(input('quantidade de elementos de b:'))
for i in range(0,n,1):
    x=int(input('digite o elemento de a:'))
    a.append(x)
for i in range(0,m,1):
    y=int(input('digite o elemento de b:'))
    b.append(y)
valor=iguais
print(valor)