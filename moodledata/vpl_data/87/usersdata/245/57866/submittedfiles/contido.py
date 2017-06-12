# -*- coding: utf-8 -*-
def iguais(a,b):
    cont=0
    for i in range(0,len(a),1):
        if a[i] in b:
            cont=cont+1
    return(cont)
n=int(input('Digite o tamanho da lista a:'))
a=[]
for i in range(1,n+1,1):
    valor=float(input('Digite o valor de a:'))
    a.append(valor)
m=int(input('Digite o tamanho da lista b:'))
b=[]
for i in range(1,m+1,1):
    valor=float(input('Digite o valor de b:'))
    b.append(valor)
resultado=iguais(n,m)
print(resultado)
