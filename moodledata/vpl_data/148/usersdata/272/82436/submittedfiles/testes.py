# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

def raiz_quadrada(x,epsilon):
    r=x
    while True:
        rq=(1/2)*(r+(x/r))
        r=rq
        if ((rq-r)<epsilon) and ((rq-r)>((-1)*epsilon)):
            return(rq)
            break
a=float(input('Digite o valor de x: '))
b=float(input('Digite o valor da precisão: '))

print(raiz_quadrada(a,b))