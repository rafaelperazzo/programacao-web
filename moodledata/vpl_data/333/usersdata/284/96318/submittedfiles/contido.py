# -*- coding: utf-8 -*-

def termocomum(lista1,lista2):
    cont=0
    for i in range(0,len(lista2),1):
        if lista2[i] in lista1:
            cont=cont+1
    return(cont)
        
lista1=[]
lista2=[]

n1=int(input('digite o numero de elementos da lista1: '))
n2=int(input('digite o numero de elementos da lista2: '))

for i in range(0,n1,1):
    lista1.append(int(input('digite um valor%.d para lista1: ' %(i+1))))

for i in range(0,n2,1):
    lista1.append(int(input('digite um valor%.d para lista2: ' %(i+1))))
print(termocomum(lista1,lista2))




