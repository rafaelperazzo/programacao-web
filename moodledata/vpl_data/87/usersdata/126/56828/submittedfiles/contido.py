# -*- coding: utf-8 -*-


def elementosiguais(a,b):
    con=0
    i=0
    for i in range(0,len(a),1):
        for i in range(0,len(b),1):
            if a[i]==a[b]:
                cont=cont+1
            i=i+1
        i=i+1
    return(cont)
n=int(input('digite a quantidade de elementos da lista 1:'))
m=int(input('digite a quantidade de elementos da lista 2:'))
x=[]
y=[]
for i in range(0,n,1):
    p=int(input('digite um valor para a lista 1:'))
    x.append(p)
    i=i+1
for i in range(0,m,1):
    q=int(input('digite um valor para a lista 2:'))
    y.append(q)
    i=i+1
print(elementosiguais(x,y))
    
    
    
    
    