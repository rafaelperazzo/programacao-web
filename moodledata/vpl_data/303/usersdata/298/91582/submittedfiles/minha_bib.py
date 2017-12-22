# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO

def algarismos(n):
    alg=1
    while (n//10)>0:
        n=n//10
        alg=alg+1
    return alg
    
def fatorial(n):
    f=1
    for i in range(1,n+1,1):
        f=f*i
    return f