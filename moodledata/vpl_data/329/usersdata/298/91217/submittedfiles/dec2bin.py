# -*- coding: utf-8 -*-

def algarismos(n):
    alg=1
    while (n//10)>0:
        n=n//10
        alg=alg+1
    return alg

def numerosden(n):
    alg=1
    while (n//10)>0:
        n=n//10
        alg=alg+1
    
    inicial=n//(10^(alg-1))
    lista=[]
    while (n%10)>0:
        k=n%10
        lista=lista+[k]
        n=n//10
    lista=lista+[inicial]
    
    listainv=[]
    for u in range (len(lista), 0, 1):
        listainv=listainv+[lista[u-1]]
    return listainv
    
K=numerosden(23456789)
print(K)

p = int(input('Digite o número p: '))
q = int(input('Digite o número q: '))

if algarismos(p)<=algarismos(q):
    

if algarismos(p)>algarismos(q):
    print('N')