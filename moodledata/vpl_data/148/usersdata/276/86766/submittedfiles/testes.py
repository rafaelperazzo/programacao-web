# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

n = 100

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

while (n<=999):
    if (primo(n)==True):
        print (n)
    n = n + 1