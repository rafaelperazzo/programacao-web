# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
def helo_world():
    print("Olá mundo")
    return
def fatorial(n):
    f=1
    for i in range(2,n+1,1):
        f*=i
    return f
def cronometro(s):
    for i in range(s,-1,-1):
        print("%d segundos" %i)
        time.sleep(1)
    print("ACABOU")
def s(x):
    x+=2
    return x
    