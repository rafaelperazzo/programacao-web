# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n = int(input('Digite o valor de n:'))
def modulo (x):
    if (x>=0):
        modulo = x
    else:
        modulo = -x
    return (modulo)
    
print (modulo(n))