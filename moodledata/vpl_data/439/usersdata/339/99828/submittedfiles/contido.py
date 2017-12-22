# -*- coding: utf-8 -*-

def elementoigual(lista1,lista2):
    soma=0
    while i in lista2:
        str(lista2[i])
    while l in lista1:
        str(lista1[l])
    if str(lista1[l])==str(lista2[i]):
        soma+=1
    else:
        soma+=0
    print (soma)
    
n=int(input('Quantidade de elementos em a: '))
m=int(input('Quantidade de elementos em b: '))
a=[]
b=[]

for i in range(0,n):
    a.append(int(input('Elemento para a:')))
    
for i in range(0,m):
    b.append(int(input('Elemento para b:')))
    
elementoigual(a,b)
    
