# -*- coding: utf-8 -*-

def pico(lista):
    cont=0
    for i in range(1,len(lista),1):
        #analisar os elementos antes do pico
        if lista[i-1]<lista[i]:
            cont+=0
            continue
        #se há algum elemento igual em sequencia
        elif lista[i-1]==lista[i]:
            cont+=1
            return('N')
            break 
        #analisar os elementos após o pico
        elif lista[i-1]>lista[i]:
            cont+=0
            continue
        else:
            cont+=1
            return('N')
            break
    #retorno caso a sequencia seja pico
    if cont==0:
        return('S')
    else:
        return('N')
    


n = input('Digite a quantidade de elementos da lista: ')
for i  in range(0,n,1):
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#CONTINUE...
