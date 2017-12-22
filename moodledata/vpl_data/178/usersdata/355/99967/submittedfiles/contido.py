# -*- coding: utf-8 -*-
n=int(input('Digite a quantidade de elementos de a: '))
m=int(input('Digite a quantidade de elementos de b: '))
a=[]
b=[]
for a in range(0,n,1):
    num=int(input('Digite um elemento de a: '))
    a.append(num)
for b in range(0,m,1):
    num=int(input('Digite um elemento de b: ')) 
    b.append(num)

if m>n:
    cont=0
    for i in range(0,m,1):
        if a[i] in b:
            cont=cont+1
    print(cont)
    
else:
    cont=0
    for i in range(0,n,1):
        if a[i] in b:
            cont=cont+1
        print (cont)
        
    
    

