# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
import timeit

def primo(n):
    cont = 0
    for i in range(2,n,1):
        if n%i==0:
            cont = cont +1
    if cont==0:
        return true
    else:
        return false
        
def soma(a,b):
    return (a+b)

#Testa o código do numero primo, 1 vez, para o número 13.000.000
t = timeit.Timer(stmt="cronometrar.primo(13.000000)",setup="import cronometrar")
print(t.timeit(1))

#Executa 13.000.000 de operações de soma
t = timeit.Timer(stmt="cronometrar2.soma(1,1)",setup="import cronometrar2")
print(t.timeit(13000000))

