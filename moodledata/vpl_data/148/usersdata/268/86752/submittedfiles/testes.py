# -*- coding: utf-8 -*-

n=int(input( huifdhwiu : '))

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
        print(False)
        

print  (primo(n))