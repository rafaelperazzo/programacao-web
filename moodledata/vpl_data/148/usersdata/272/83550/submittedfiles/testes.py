# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

def raiz_quadrada(x,epsilon):
    r=x
    while True:
        rq=(1/2)*(r+(x/r))
        if (abs(r-rq)<epsilon):
            return(rq)
        r=rq
a=float(input('Digite o valor de x: '))
b=float(input('Digite o valor da precisao: '))

print(raiz_quadrada(a,b))