# -*- coding: utf-8 -*-
def inter(x,y):
    cont=0
    for i in range(0,len(x),1):
        for j in range(0,len(y),1):
            if x[i]==y[j]:
                cont=cont+1
    return(cont)


n=int(input('Quantidade de elementos de "a": '))
b=int(input('Quantidade de elementos de "b": '))
a=[]
b=[]
for i in range(0,n,1):
    a.append(float(input('Digite os elementos de "a": ')))
for i in range(0,m,1):
    b.append(float(input('Digite os elementos de "b": ')))
print(inter(a,b))