# -*- coding: utf-8 -*-
def pico(lista):
    cont_a = 0
    cont_b = 0
    for i in range(0,len(lista)-1,1):
        if lista[i]<lista[i+1]:
            cont_a = cont_a + 1
        else:
            break
    for i in range(cont_a,len(lista)-1,1):
        if lista[i]>lista[i+1]:
            cont_b = cont_b + 1
        else:
            break    
    if cont_a + cont_b == len(lista)-1 and cont_a>0 and cont_b>0:
        return('S')
    else:
        return('N')
lista=[]
n = int(input('Digite a quantidade de elementos da lista: '))
for i in range(0,n,1):
    lista.append(int(input('Digite n: ')
print (lista)
        