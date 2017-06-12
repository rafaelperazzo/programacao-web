# -*- coding: utf-8 -*-
def iguais (a,b):
    cont=0
    for i in range (0,len(a)-1,1):
        if a[i] in b:
            cont=cont+1
    return cont
n=int(input('tamanho de n:'))
m=int(input('tamanho de m:'))
x=[]
y=[]
for i in range (0,ln,1):
    a=int(input('valor p n:'))
    x.append(a)
for i in range (0,m,1):
    b=int(input('valor p m:'))
    x.append(b)
print (n)
print (m)
print (iguais(x,y))


