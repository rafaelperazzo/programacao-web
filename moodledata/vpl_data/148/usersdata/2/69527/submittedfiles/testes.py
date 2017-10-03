# -*- coding: utf-8 -*-

import timeit

def primo(n):
    cont = 0
    for i in range(2,n,1):
        if n%i==0:
            cont = cont +1
    if cont==0:
        return True
    else:
        return False
    
def soma(a,b):
    return (a+b)    

#Testa o codigo do numero primo, 1 vez, para o numero 13.000.000
t = timeit.Timer(stmt="testes.primo(13000000)",setup="import testes")
print(t.timeit(1))

#Executa 13.000.000 de operaçoes de soma
t = timeit.Timer(stmt="testes.soma(1,1)",setup="import testes")
print(t.timeit(13000000))