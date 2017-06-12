# -*- coding: utf-8 -*-

def pico(lista):
    cont=0
    for i in range (0,len(lista)-1,1):
        if lista[i]<lista[i+1]<lista[i+2]:
            cont=cont+1
            return True
        else:
            return(False)
    

n = int(input('Digite a quantidade de elementos da lista: '))
a=[]
for i in range(1,n+1,1):
    valor=int(input('Digite o elemento da lista: '))
    a.append(valor)
    
if pico(a)==True:
    print('S')
else:
    print('N')
#CONTINUE...
