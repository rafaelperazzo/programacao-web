# -*- coding: utf-8 -*-

def pico(lista):
    #CONTINUE...
    cont=0
    for i in range (0,len(lista),1):
        if lista[i]<lista[i-1] and lista[i]>lista[i+1]:
            cont=cont+1
        elif lista[i]>lista[i-1] and lista[i]<lista[i-1]:
            cont=cont+1
    if cont!=0:
        return True
    else:
        return False
        
n=int(input('Digite a quantidade de elementos da lista: '))
#/CONTINUE...
lista=[]
for i in range (0,n,1):
    lista.append(int(input('valores da lista:')))
resultado=pico(lista)
if resultado==True:
    print('S')
else:
    print('N')
    
