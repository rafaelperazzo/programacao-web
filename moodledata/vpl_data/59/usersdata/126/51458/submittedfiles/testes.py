# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

def primo(n):
    cont=0
    for i in range (2,n,1):
        if n%2==0:
            cont=cont+1
    if cont==0:
        return(True)
        
    else:
        return(False)
soma=0
a=3
if primo(a):
    soma=1+a
    print(soma)
else:
    print('n')