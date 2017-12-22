# -*- coding: utf-8 -*-
#FUNÇÃO
def lecker(a):
    cont=0
    if a[0]>a[1]:
        cont=cont+1
    if a[len(a)-1]>a[len(a)-2]:
        cont=cont+1
    for i in range(1,len(a)-1,1):
        if a[i]>a[i+1] and a[i]>a[i-1]:
            cont=cont+1
    if cont==1:
        return('S')
    else:
        return('N')
    

#PROGRAMA PRINCIPAL
n=int(input('Número de elementos: '))
a=[]
b=[]
for i in range(0,n,1):
    print()
    print('LISTA 1: ')
    a.append(int(input('Digite os elementos: ')))
for i in range(0,n,1):
    print()
    print('LISTA 2: ')
    b.append(int(input('Digite os elementos: ')))
print(lecker(a))
print(lecker(b))

