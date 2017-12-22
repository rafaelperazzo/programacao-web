# -*- coding: utf-8 -*-

def crescente (lista):
    cont = 0
    if i==0:
        if lista[1]>lista[0]:
           cont = cont +1
           
    elif i == len(lista)-1:
        if lista[len(lista)-1] > lista[len (lista)-2]:
                cont = cont +1
            
    else:
        if lista[i-1]<lista[i]<lista[i+1]:
                cont = cont +1
    
    if cont == len (lista):
        return (True)
    else:
        return (False)
        
def decrescente (lista):
    cont = 0
    if i==0:
        if lista[1]<lista[0]:
           cont = cont +1
           
    elif i == len(lista)-1:
        if lista[len(lista)-1] < lista[len (lista)-2]:
                cont = cont +1
            
    else:
        if lista[i-1]>lista[i]>lista[i+1]:
                cont = cont +1
    
    if cont == len (lista):
        return (True)
    else:
        return (False)    
        

def pico(lista):
    indice_maior = a.index[max(a)]
    for i in range (0,indice_maior,1):
        elemento_antes = a[i]
        antes = []
        antes.append (elemento_antes)
    
    for i in range (indice_maior + 1,len (a),1):
        elemento_depois = a[i]
        depois = []
        depois.append (elemento_depois)
    
    if crescente (antes) and decrescente (depois):
        return (True)
    else:
        return (False)
    #CONTINUE...

n = input('Digite a quantidade de elementos da lista: ')
#CONTINUE...
a = []
for i in range (0,n,1):
    a.append ('input('Digite o elemento da lista: '))')

print (pico (a))
    