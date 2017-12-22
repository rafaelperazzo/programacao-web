# -*- coding: utf-8 -*-

def crescente (lista):
    cont = 0
    for i in range (0,len(lista),1):
        if i==0:
            if lista[0]<lista[1]:
                cont = cont +1
           
        elif i == len(lista)-1:
            if lista[len(lista)-2] < lista[len (lista)-1]:
                cont = cont +1
            
        else:
            if lista [i-1]<lista[i]<lista[i+1]:
                cont = cont +1
    
    if cont == len (lista):
        return (True)
    else:
        return (False)
        
def decrescente (lista):
    cont = 0
    for i in range (0,len(lista),1):
        if i==0:
            if lista[0]>lista[1]:
                cont = cont +1
           
        elif i == len(lista)-1:
            if lista[len(lista)-2] > lista[len (lista)-1]:
                cont = cont +1
            
        else:
            if lista [i-1]>lista[i]>lista[i+1]:
                cont = cont +1
    
    if cont == len (lista):
        return (True)
    else:
        return (False)    
        

def pico(lista):
    elemento_maior = max(lista)
    indice_maior = lista.index(elemento_maior)
    for i in range (0,indice_maior,1):
        elemento_antes = lista[i]
        antes = []
        antes.append (elemento_antes)
    
    for i in range (indice_maior + 1,len (lista),1):
        elemento_depois = lista[i]
        depois = []
        depois.append (elemento_depois)
    
    if crescente (antes) and decrescente (depois):
        return (True)
    else:
        return (False)
    #CONTINUE...

n = int (input('Digite a quantidade de elementos da lista: '))
#CONTINUE...
a = []
for i in range (0,n,1):
    valor_a = float (input('Digite o elemento da lista: ')) 
    a.append(valor_a)

print (pico (a))
    