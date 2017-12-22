# -*- coding: utf-8 -*-

def elementoigual(lista1,lista2):
    soma=0
    for i in range(0,len(lista1)-1):
        while lista1[i] in lista2:
            soma+=1
            break
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
    
