# -*- coding: utf-8 -*-
def lecker(lista):
    cont=0
    for i in range (0,len(lista),1):
        if i==0:
            if lista[i]>lista[i+1]:
                cont=cont+1
        elif i==len(lista)-1:
            if lista[i]>lista[i-1]:
                cont=cont+1
        else:
            if lista[i]>lista[i+1] and lista[i]>lista[i-1]:
                cont=cont+1
    return(cont) 
a=[]
b=[]
n=int(input('quantidade de elementos das listas:'))
for i in range (0,n,1):
    a.append(int(input('elementos de a:')))
for i in range (0,n,1):
    b.append(int(input('elementos de b:')))
resultado1=lecker(a)
resultado2=lecker(b)
if resultado1==1:
    print('S')
else:
    print
if resultado2==1:
    print('S')
else:
    print('N')    