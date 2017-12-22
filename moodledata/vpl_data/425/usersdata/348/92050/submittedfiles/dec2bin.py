# -*- coding: utf-8 -*-

#contador de digitos 
def ContaDigitos (n):
    cont = 1 
    while (n//10>0):
        n = n//10
        cont += 1
    return cont

# somar digitos
def somardigitos(g):
    soma = 0
    while g is not 0:
        soma += g%10
        g = g/10
    return soma 

print(somardigitos(23))
'''
p = int(input('informe o p: '))
q = int(input('informe o q: '))

if somardigitos(p) <=  ContaDigitos(q):
    print ('S')
else:
    print('N')
'''

        

