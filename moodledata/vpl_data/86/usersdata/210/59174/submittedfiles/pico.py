# -*- coding: utf-8 -*-


def pico(z):
    for i in range(0,len(z)-1,1):
        decr=0
        cres=0
        if i=0:
            if z[i]<z[i+1]:
                cres=cres+1
            else:
                break
            else:
                decr=decr+1
            
    
    
    
    
    if cres>0 and decr>0:
        return(true)
    else:
        return(false)
        
        
        
        
A= input('Digite a quantidade de elementos da lista: ')
b=[]
for i in range(0,A,1):
    c=int(input('digite o valor:'))
    b.append(c)
    
if pico(b):
    print('s')
else:
    print('N')
    
    
