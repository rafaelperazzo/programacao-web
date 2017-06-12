# -*- coding: utf-8 -*-
p=[]
q=[]
r=[]
i=0
def crescente (a):
    cont=0
    i=0
    for i in range(1,len(a)-1,1):
        if a[i]<a[i+1]:
            cont=cont+1
    if cont==(len(a)-1):
        return True
def decrecente (a):
    cont=0
    i=0
    for i in range(1,len(a)-1,1):
        if a[1]>a[i+1]:
            cont=cont+1
    if cont==(len(a)-1):
        return True
def consecutivosiguais (a):
    cont=0
    i=0
    for i in range(1,len(a)-1,1):
        if a[i]==a[i+1]:
            cont=cont+1
    if cont>0:
        return True

n=int(input('digite n:')


for i in range(0,n,1):
    valor=float(input('digite o valor:')
    p.append(valor)
    
for i in range(1,n+1,1):
    valor=float(input('digite o valor:')
    q.append(valor)
    
for i in range(1,n+1,1):
    valor=float(input('digite o valor:')
    r.append(valor)
    




#escreva o programa principal
