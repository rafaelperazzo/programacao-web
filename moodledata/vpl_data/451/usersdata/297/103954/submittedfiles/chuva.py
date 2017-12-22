# -*- coding: utf-8 -*-
n=int(input('digite o número de seções que a piscina tem: '))
while n<1 or n>10**5:
   n=int(input('digite o número de seções que a piscina tem: ')) 
lista=[]
for i in range(0,n,1):
    Hi=int(input('digite a o elemento altura da seção%d: '%(i+1)))
    while Hi<1 or Hi>10**9:
        Hi=int(input('digite a o elemento altura da seção%d: '%(i+1)))
    lista.append(Hi)
borda1=lista[i]
borda2=lista[n-1]
if borda1<=borda2:
    s1=sum(lista)
    print(sum(lista))
    t1=lista[i]*n
    agua1=t1-s1
    print(agua1)
else :
    s2=sum(lista)
    t2=lista[n-1]*n
    agua2=t2-s2
    print(agua2)
