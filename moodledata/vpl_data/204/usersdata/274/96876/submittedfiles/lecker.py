# -*- coding: utf-8 -*-
def lecker(a):
    cont=0
    if a[0]>a[1]:
        cont=cont+1
    for i in range (1,len(a)-1,1):
        if a [i-1]<a[i] and a[i]>a[i+1]:
            cont=cont+1
    if a[len(a)-1]>a[len(a)-2]:
        cont=cont+1
    if cont==1:
        return(1)
    else:
        return(0)

n=int(input("Digite um valor: "))
a=[]
for r in range (0,n,1):
    x=int(input("Digite um valor: "))
    a.append(x)
b=[]
for r in range (0,n,1):
    x=int(input("Digite um valor: "))
    b.append(x)
if lecker(a)==1:
    print("S")
else:
    print("N")
if lecker(b)==1:
    print("S")
else:
    print("N")

