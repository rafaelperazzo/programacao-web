# -*- coding: utf-8 -*-

def pico(lista):
    x=[]
    n=len(lista)
    for i in range (0,n-1,1):
        if (lista[i] > lista [i+1]):
            x.append(1)
        if (lista[i] < lista [i+1]):
            x.append(2)
        if (lista[i]==lista[i+1]):
            x.append(0)
    
    k= sorted(x)   
    
    if (x==k):
        if (0 in x ):
            print("N") 
        else :
            print ("S")
        
        
        
        

def entrada_user(n):
    lista=[]
    for i in range (0,n,1):
        lista.append(int(input("Digite o %d elemeto para o seu vetor:" %(n+1))))
    return lista
    
        
    
  # PROGRAMA PRINCIPAL 
n = input('Digite a quantidade de elementos da lista: ')  
entrada_user(n)
pico(lista)
    
    
