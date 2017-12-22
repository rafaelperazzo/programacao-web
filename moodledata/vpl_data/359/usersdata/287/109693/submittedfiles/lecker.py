# -*- coding: utf-8 -*-
def lecker(lis):
    cont=0
    for i in range (1,len(lis)-1):
        if lis[i]>lis[i+1] and lis[i]>lis[i-1]:
            cont+=1
    if lis[0]>lis[1] or lis[len(lis)-1]>lis[len(lis)-2]:
        cont+=1
    return(cont)
        
q1=int(input('digite os elementos da primeira lista: '))
q2=int(input('digite os elementos da segunda lista: '))
lista1=[]
lista2=[]
for i in range (0,q1):
    lista1.append(int(input('digite o valor')))
for i in range (0,q2):
    lista2.append(int(input('digite os valores da lista 2')))

cont=lecker(lista1):
if cont!=1:
    print('N')
elif cont==1:
    print('S')
cont=lecker(lista2)
if cont!=1:
    print('N')
elif cont==1:
    print('S')
        
        


