# -*- coding: utf-8 -*-
def termocomum(lista1,lista2):
    cont=0
    for i in range(0,len(lista2),1):
        if lista2[i] in lista1:
            cont=cont+1
    return(cont)

n=int(input('digite a quantidade de termos da lista a: '))
m=int(input('digite a quantidade de termos da lista b: '))
a=[]
b=[]
for i in range(0,n,1):
    valorA=float(input('digite os termos da lista a: '))
    a.append(valorA)
for i in range(0,n,1):
    valorB=float(input('digite os termos da lista b: '))
    b.append(valorB)
    
print(termocomum(a,b))