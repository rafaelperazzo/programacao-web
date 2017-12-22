# -*- coding: utf-8 -*-
n=int(input('digite o numero de secoes que a piscina tem: '))
while n<1 or n>10**5:
   n=int(input('digite o numero de secoes que a piscina tem: ')) 
lista=[]
for i in range(0,n,1):
    Hi=int(input('digite a o elemento altura da secao: '))
    while Hi<1 or Hi>10**9:
        Hi=int(input('digite a o elemento altura da secao: '))
    lista.append(Hi)
borda1=lista[i]
borda2=lista[n-1]
cont=0
if borda1<=borda2:
    for i in range(0,n,1):
        if borda1>lista[i]:
            cont=cont+1
else :
    for i in range(0,n,1):
        if borda2<lista[i]:
            cont=cont+1
print(cont)
