# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

n = int(input('Digite n: '))

def primo (x):
    i = 2
    cont = 0
    while (i<x):
        if (x%i==0):
            cont = cont +1
            break
        else:
            i = i + 1
    if (cont == 0):
        return (True)
    else:
        return (False)

numero = primo(n)
print (numero)