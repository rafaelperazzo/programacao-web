# -*- coding: utf-8 -*-

def pico(x):
    for i in range(0,len(x),1):
        cont=0
        cont1=0
        if x[i]>x[i+1]:
            break
        else:
            if x[i]<x[i+1]:
                cont=cont+1
                i=i+1
                if x[i]>x[i+2]:
                    cont1=cont1+1
                    i=i+1
                
    if cont>1 and cont2>1:
        return True
    else:
        return False
            
    
    


n = input('Digite a quantidade de elementos da lista: ')
a=[]
for i in range(0,n,1):
    d=int('Digite o valor:')
    a.append(d)