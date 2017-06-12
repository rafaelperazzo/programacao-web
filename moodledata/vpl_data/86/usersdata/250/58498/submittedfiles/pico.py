# -*- coding: utf-8 -*-

def pico(lista):
    #CONTINUE...
    cont=0
    for i in range (0,len(lista),1):
        if lista[i]>lista[i-1] and lista[i]>lista[i+1]:
            cont=cont+1
        elif lista[i]>lista[i-1] and lista[i]<lista[i-1]:
            cont=cont+1
    if cont==0:
        return False
    else:
        return True
n=int(input('Digite a quantidade de elementos da lista: '))
#/CONTINUE...
lista=[]
for i in range (0,n,1):
    lista.append(int(input('valores da lista:')))
if pico(lista):
    print('S')
else:
    print('N')
    
