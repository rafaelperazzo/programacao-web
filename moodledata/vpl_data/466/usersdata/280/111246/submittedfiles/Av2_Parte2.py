# -*- coding: utf-8 -*-
def cres(l):
    cont=0
    for i in range (0,len(l)-1,1):
        if l[i] < l[i+1]:
            cont=cont+1
    if cont==(len(l)-1):
        an=("S")
    else:
        an=("N")
    return an
    
def decres(l):
    cont=0
    for i in range (0,len(l)-1,1):
        if l[i] > l[i+1]:
            cont=cont+1
    if cont==(len(l)-1):
        an=("S")
    else:
        an=("N")
    return an
    
def iguais(l):
    cont=0
    for i in range (0,len(l)-1,1):
        if l[i] == l[i+1]:
            cont=cont+1
    if cont != 0:
        an=("S")
    else:
        an=("N")
    return an

n=int(input("Digite n: "))
a=[]
b=[]
c=[]
for i in range(0,n,1):
    a.append("Digite um valor: ")
    
for i in range(0,n,1):
    b.append("Digite um valor: ")
    
for i in range(0,n,1):
    c.append("Digite um valor: ")
    
print(cres(a))
print(decres(a))
print(iguais(a))
print(cres(b))
print(decres(b))
print(iguais(b))
print(cres(c))
print(decres(c))
print(iguais(c))