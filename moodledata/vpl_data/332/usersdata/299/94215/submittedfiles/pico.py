# -*- coding: utf-8 -*-
def pico(lista):
    a=[]
    b=[]
    for i in range(1,len(lista),1):
        #analisar os elementos antes do pico
        if lista[i-1]<lista[i]:
            a.append(lista[i])
        elif lista[i-1]==lista[i]:
            return('N')
            break
        elif lista[i-1]<lista[i]:
            b.append(lista[i])
    return(a)
    return(b)
            
           
    #retorno caso a sequencia seja pico


l=[]
n = int(input('Digite a quantidade de elementos da lista: '))
for i  in range(0,n,1):
    l.append(int(input('')))
print(pico(l))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#CONTINUE...
