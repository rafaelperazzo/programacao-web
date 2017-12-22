# -*- coding: utf-8 -*-
lista=[]
def mod_dif(x,y):
    dif=x-y
    if dif<0:
        return(dif*-1)
    else:
        return(dif)
    
    
    
    
    
degrau=0
n=int(input('digite o numero de termos: '))
while (n<2):
    n=int(input('digite o numero de termos: '))
    
for i in range(0,n,1):
    lista.append(int(input('digite o valor%.d: ' %(i+1))))
    
for i in range(0,len(lista)-1,1):
    if mod_dif(lista[i],lista[i+1])>degrau:
        degrau=mod_dif(lista[i],lista[i+1])
    print(degrau)















