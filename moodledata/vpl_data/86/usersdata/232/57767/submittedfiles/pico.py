# -*- coding: utf-8 -*-

def pico(lista):
    cont1=0
    cont2=0
    metade=0
    if len(lista)%2==0:
        metade=(len(lista)-2)/2
    else:
        metade-(len(lista)-1)/2
    for i in range(1,metade+1,1):
        if lista[i]<lista[i-1]:
            cont1=cont+1
            break
    for i in range(metade+1,len(lista),1):
        if lista[i]>lista[i-1]:
            cont=cont+1
            break
    if cont1+cont2==0:
        return(True)
    else:
        return(False)
    #CONTINUE...
    

    

a=[]
n =int(input('Digite a quantidade de elementos da lista: '))
#CONTINUE...
for i in range(1,n+1,1):
    h=int(input('Digite o valor do termo '+str(i)+' da lista: '))
    a.append(h)

if pico(a):
    print('S')
else:
    print('N')