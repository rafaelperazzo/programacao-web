# -*- coding: utf-8 -*-
def somaip(a):
    som1=0
    som2=0
    for i in range(0,len(a),1):
        if a[i]%2!=0:
            som1=som1+a[i]
        else:
            som2=som2+a[i]
        return(som1)
        return(som2)
print(somaip(lis))
lis=[]
n=int(input('Digite o tamanho da lista:'))
for i in range(1,n+1,1):
    va=float(input('Digite o valor do elemento:'))
    lis.append(va)
print(somaip(lis))