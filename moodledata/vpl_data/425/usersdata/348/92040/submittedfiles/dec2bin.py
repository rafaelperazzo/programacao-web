# -*- coding: utf-8 -*-

#contador de digitos 
def ContaDigitos (n):
    cont = 1 
    while (n//10>0):
        n = n//10
        cont += 1
    return cont

p = int(input( 'informe o p: '))
q = int(input( 'informe o q: '))



