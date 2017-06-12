# -*- coding: utf-8 -*-
def correspondente(a,b):
    c=[]
    for i in range (0,len(a),1):
        if a[i] in b:
            c.append(a[i])
    return (c)
    
a=[]
b=[]
n=int(input('Digite a quantidade de elementos de a: '))
m=int(input('Digite a quantidade de elementos de b: '))

for i in range (1,n+1,1):
    h1=int(input('Digite o elemento '+str(i)+' da lista a: '))
    a.append(h1)

for i in range (1,m+1,1):
    h2=int(input('Digite o elemento '+str(i)+' da lista b: '))
    b.append(h2)
    
print(len(c))


