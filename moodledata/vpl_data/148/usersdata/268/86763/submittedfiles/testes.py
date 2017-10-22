# -*- coding: utf-8 -*-

def primo(x):
    cont=0
    i=2
    while(i<n):
        divisao= x%i
        if divisao==0:
            cont=cont+1
            break
        else:
            i=i+1
    if cont==0:
        return(True)
    if cont!=0:
        return(False)
        
        
for i in range(100,1000,1):
    if primo(i)==True:
        print(i)
    