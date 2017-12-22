# -*- coding: utf-8 -*-
def lecker(lis):
    cont=0
    for i in range (1,len(lis)-1):
        if lis[i]>lis[i+1] and lis[i]>lis[i-1]:
            cont+=1
    if lis[0]>lis[1] or lis[len(lis)-1]>lis[len(lis)-2]:
        cont+=1
    return(cont)

q1=int(input("Digite a quantidade de elementos da lista1: "))
q2=int(input("Digite a quantidade de elementos da lista2: "))
lista1=[]
lista2=[]
for i in range(0,q1,1):
    lista1.append(int(input("Digite o valor: ")))
for i in range(0,q2,1):
    lista2.append(int(input("Digite o valor: ")))
cont=lecker(lista1)
if cont!=1:
    print('N')
elif cont==1:
    print('S')
    
cont=lecker(lista2)
if cont!=1:
    print('N')
elif cont==1:
    print('S')

