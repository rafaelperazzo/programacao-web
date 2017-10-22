# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

def primo(x):
    i=2
    cont=1
    while (i<x):
        if ((x%i)==0):
            return (False)
        else:
            i=i+1
            cont=cont+1
    if (cont!=0):
        return (True)
        
for i in range (100,1000,1):
    if (primo(i)):
        print(i)

