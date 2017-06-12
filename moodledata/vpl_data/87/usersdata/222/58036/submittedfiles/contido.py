# -*- coding: utf-8 -*-
def intersecção(listaA,listaB):
    cont=0
    ind=0
    if len(listaA)<len(listaB):
        while ind<len(listaA):
            for j in range(0,len(listaB),1):
                if listaA[ind]==listaB[j]:
                    cont=cont+1
            ind=ind+1
    else:
        while ind<len(listaB):
            for i in range(0,len(listaA),1):
                if listaB[ind]==listaA[j]:
                    cont=cont+1
            ind=ind+1
    return cont
n=int(input('n:'))
m=int(input('m:'))
lista1=[]
lista2=[]
for i in range(n):
    a=float(input('a:'))
    lista1=lista1+[a]
for i in range(m):
    b=float(input('b:'))
    lista2=lista2+[b]
c=intersecção(lista1,lista2)
print(c)

