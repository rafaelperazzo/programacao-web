# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
def hello_word():
    print("Olá mundo")
    return

def fatorial(n):
    f=1
    for i in range (1,n+1,1):
        f*=i
        print("Estou no %.d" %(f))