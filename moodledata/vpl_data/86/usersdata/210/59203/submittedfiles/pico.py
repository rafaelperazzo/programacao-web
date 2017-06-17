# -*- coding: utf-8 -*-


def pico(x):
    for i in range(0,len(x)-1,1):
        decr=0
        cres=0
        if i==0:
            if x[i]<x[i+1]:
                cres=cres+1
            else:
                break
        else:
            if x[i]<x[i+1]:
                cres=cres+1
            else:
                decr=decr+1
            
    
    if cres>0 and decr>0:
        return(true)
    else:
        return(false)
        
        
        
        
a= int(input('Digite a quantidade de elementos da lista: '))
b=[]
for i in range(0,a,1):
    c=int(input('digite o valor:'))
    b.append(c)
    
if pico(b):
    print('s')
else:
    print('N')
    
    
