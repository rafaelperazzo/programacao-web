# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
#def multiplicacao(x,y):
#    m= x * y
#   return m
def fatorial(n):
    f=1
    for i in range(2,n+1,1):
        f*=i
    return f
    
def cronometro(s):
    for i in range(s,-1,-1):
        print ("%d segundos" %i)
        time.sleep(1)
        return s