# -*- coding: utf-8 -*-

def algarismos(n):
    alg=1
    while (n//10)>0:
        n=n//10
        alg=alg+1
    return alg

def numerosden(n):
    pr=n
    alg=1
    while (n//10)>0:
        n=n//10
        alg=alg+1
    
    inicial=pr//(10^(alg-1))
    lista=[]
    while (pr%10)>0:
        k=pr%10
        lista=lista+[k]
        pr=pr//10
    
    listainv=[]
    for u in range (len(lista), 0, -1):
        jj=lista[u-1]
        listainv=listainv+[jj]
    return listainv


p = int(input())
q = int(input())

if algarismos(p)<=algarismos(q):
    listadep=numerosden(p)
    listadeq=numerosden(q)
    listacomparacao=[y for y in listadep if y in listadeq]
    b=str()
    for x in range(0, len(listacomparacao)-1)
        b=b+str(listacomparacao[x])

    print(listacomparacao)
    if b==p:
        print('S')
    if not b==p:
        print('N')

if algarismos(p)>algarismos(q):
    print('N')