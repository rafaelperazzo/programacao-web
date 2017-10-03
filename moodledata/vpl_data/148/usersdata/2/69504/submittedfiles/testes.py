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
    
t = timeit.Timer(stmt="testes.primo(11700000)",setup="import testes")
print(t.timeit(1))