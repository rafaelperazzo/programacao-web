# -*- coding: utf-8 -*-

def pico(lista):
    #CONTINUE...
    cont=0
    cont2=0
    for i in range (0,len(lista),1):
        if lista[i]>lista[i-1]:
            cont=cont+1
        if lista[i]>lista[i+1]:
            cont2=cont2+1
    if cont!=0 and cont2!=0:
        return True
    else:
        return False
        
n=int(input('Digite a quantidade de elementos da lista: '))
#/CONTINUE...
lista=[]
for i in range (0,n,1):
    lista.append(int(input('valores da lista:')))
if pico(lista)==True:
    print('S')
else:
    print('N')
    
