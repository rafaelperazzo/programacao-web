# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

def raiz_quadrada(x,epsilon):
    r=x
    while True:
        rq=(1/2)*(r+(x/r))
        r=rq
        if ((rq-r)<epsilon) and ((rq-r)>(-epsilon)):
            return(rq)
            break
        
    
a=int(input('Digite o valor de x: '))
b=int(input('Digite o valor da precisão: '))

print(raiz_quadrada(a,b))