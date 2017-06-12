# -*- coding: utf-8 -*-

def pico(lista):
    cont=0
    #CONTINUE...
    for i in range(0,len(lista),1):
        if lista[0]>=lista[1]:
            cont=cont+1
        if lista[i]<=lista[i+1]:
            cont=cont+1
    return (cont)


n = int(input('Digite a quantidade de elementos da lista: '))
a=[]
for i in range(0,n,1):
    b=int(input('b:'))
    a.append(b)
        
if pico==2:
    print('S')
else:
    print('N')

#CONTINUE...
