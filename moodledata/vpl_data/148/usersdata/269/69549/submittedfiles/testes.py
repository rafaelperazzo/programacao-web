# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
import timeit

def primo(n):
    cont = 0
    for i in range(2,n,1:
        if n%i==0:
            cont = cont +1
    if cont==0:
        return True
    else:
        return False
        
def soma(a,b:
    return (a+b)
    
t = timeit.Timer(stmt='cronometrar.primo(13000000)',setup='import cronometrar')
print(t.timeit(1))

t = timeit.Timer(stmt='cronometrar2.soma(1,1)',setup='import cronometrar2')
print(t.timeit(13000000))
