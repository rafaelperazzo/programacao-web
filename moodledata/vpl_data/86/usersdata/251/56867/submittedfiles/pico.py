# -*- coding: utf-8 -*-


def pico(lista):
    cont1=1
    cont2=1
    for i in range(0,len(lista)/2,1):
        if lista[i]<lista[i-1]:
            cont1=0
            break
    
    for i in range (((len(lista)-1)/2),len(lista),1):
         if lista[i]>lista[i-1]:
            cont1=0
            break
    
    if cont1+cont2==2:
        return(True)
    
    return(False)   
    

lista=[]
n = int(input('Digite a quantidade de elementos da lista: '))
#CONTINUE...
for i in range(0,n,1):
    termo=int(input('Digite o valor do termo de índice '+str(i)+' da lista: '))
    lista.append(termo)
    
if pico(lista):
    print('S')
else:
    print('N')