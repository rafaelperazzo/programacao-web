# -*- coding: utf-8 -*-

def pico(lista):
    cont1=1
    cont2=1
    metade=0
    if len(lista)%2==0:
        metade=(len(lista)-2)/2
    else:
        metade=(len(lista-1)/2
    for i in range(1,metade+1,1):
        if lista[i]<lista[i-1]:
            cont1=0
            break
    for i in range (metade+1,len(lista),1):
        if lista[i]>lista[i-1]:
            cont2=0
            break
    if cont1+cont2==2:
        return(True)
    else:
        return(False)
        
lista=[]    
n = input('Digite a quantidade de elementos da lista: ')
for i in range(0,n,1):
    termo=int(input('digite um valor'+str(i)''))
    lista.append(termo)
    
if pico(lista):
    print('S')
else:
    print('N')