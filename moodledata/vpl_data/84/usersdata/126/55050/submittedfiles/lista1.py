# -*- coding: utf-8 -*-
a=[]
i=0
n=int(input('digite o numero de elementos da lista:'))

for i in range(1,n+1,1):
    m=int(input('digite um valor:'))
    a.append(m)
    i=i+1

def impar(p):
    for i in range(0,len(a),1):
        if i%2==1:
            return True
def par(p):
    for i in range(0,len(a),1):
        if i%2!=0:
            return True
def quantimpar(p):
cont=0
    for i in range(0,len(a),1):
        if i%2==1:
            cont+cont+1
        if cont>0:
            return(cont)
def quantpar(p):
cont=0
    for i in range(0,len(a),1):
        if i%2==0:
            cont+cont+1
        if cont>0:
            return(cont)
if impar(a):
    print

    
    
