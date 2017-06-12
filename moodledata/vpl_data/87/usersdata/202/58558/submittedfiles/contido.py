# -*- coding: utf-8 -*-
def iguais (a,b):
    cont=0
    for i in range (0,len(a)-1,1):
        if a[i] in b:
            cont=cont+1
    return cont
l1=int(input('tamanho da l1:'))
l2=int(input('tamanho da l2:'))
x=[]
y=[]
for i in range (0,l1,1):
    a=int(input('valor l1:'))
    x.append(a)
for i in range (0,l2,1):
    b=int(input('valor l2:'))
    x.append(b)
print (l1)
print (l2)
print (iguais(x,y))


