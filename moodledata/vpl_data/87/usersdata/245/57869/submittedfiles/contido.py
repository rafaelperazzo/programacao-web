# -*- coding: utf-8 -*-
def iguais(a,b):
    cont=0
    for i in range(0,len(a),1):
        if a[i] in b:
            cont=cont+1
    return(cont)
n=int(input('Digite o tamanho da lista a:'))
m=int(input('Digite o tamanho da lista b:'))
a=[]
for i in range(1,n+1,1):
    valor=int(input('Digite o valor de a:'))
    a.append(valor)
b=[]
for i in range(1,m+1,1):
    valor=int(input('Digite o valor de b:'))
    b.append(valor)
resultado=iguais(n,m)
print(resultado)
