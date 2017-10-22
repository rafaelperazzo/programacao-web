# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
def conta_digitos(n):
    contador = 1
    while (n//10>0):
        n = n//10
        contador += 1
    return contador
print(conta_digitos(8))
print(conta_digitos(2000))
