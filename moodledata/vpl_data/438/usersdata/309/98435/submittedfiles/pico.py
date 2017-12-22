# -*- coding: utf-8 -*-

def pico(lista):
    x=[]
    n=len(lista)
    for i in range (0,n-1,1):
        if (lista[i] > lista[i+1]):
            x.append(1)
        elif (lista[i] < lista[i+1]):
            x.append(2)
        else :
            x.append(0)
    
    k= sorted(x)   
    
    if (x==k):
        if (0 in x ):
            print("N") 
        elif (1 in x and 2 in x):
            print ("S")
        else:
             print("N") 
            
        
        
    
  # PROGRAMA PRINCIPAL

n = int(input('Digite a quantidade de elementos da lista: '))  
lista=[]
for i in range (0,n,1):
    lista.append(int(input("Digite um  elemeto para o seu vetor:" )))
  
    
pico(lista)
    
    
