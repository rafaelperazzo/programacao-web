# -*- coding: utf-8 -*-
def iguais(a,b):
    cont=0
    for i in range(0,len(a),1):
        if a[i] in b:
            cont=cont+1
    
    return(cont)
    
n1=int(input('digite a quantidade de elementos de a:'))
n2=int(input('digite a quantidade de elementos de b:'))
a=[]
b=[]
for i in range(1,n1+1,1):
    valor=float(input('digite um valor:'))
    a.append(valor)
    
for i in range(1,n2,1):
    valor=float(input('digite um valor:'))
    b.append(valor)

x=iguais(a,b)    
print(x)    