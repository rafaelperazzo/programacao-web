# -*- coding: utf-8 -*-

def algarismos(n):
    alg=1
    while (n//10)>0:
        n=n//10
        alg=alg+1
    return alg

def numerosden(n):
    p=n
    alg=1
    while (n//10)>0:
        n=n//10
        alg=alg+1
    
    inicial=p//(10^(alg-1))
    lista=[]
    while (p%10)>0:
        k=p%10
        lista=lista+[k]
        p=p//10
    
    listainv=[]
    for u in range (len(lista), 0, -1):
        jj=lista[u-1]
        listainv=listainv+[jj]
    return listainv
    
K=numerosden(23456789)
print(K)
'''
p = int(input('Digite o número p: '))
q = int(input('Digite o número q: '))

if algarismos(p)<=algarismos(q):
    

if algarismos(p)>algarismos(q):
    print('N')
'''