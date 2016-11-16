#ARQUIVO COM SUAS FUNCOES
from __future__ import division
def fatorial(n):
    produto=1
    for i in range(1,n+1,1):
        produto=produto*i
    return produto

def valor_absoluto(x):
    if x<0:
        x=x*(-1)
    return x

def pi(m):
    soma=0
    j=2
    for i in range(1,m+1,1):
        if i%2==0:
            soma=soma-(4/(j*(j+1)*(j+2)))
        else:
            soma=soma+(4/(j*(j+1)*(j+2)))
        j=j+2
    soma=soma+3
    return soma


def cosseno(z,epsilon):
    iesimo=1
    cosz=1
    i=1
    j=2
    while iesimo>=epsilon:
        if i%2==0:
            cosz=cosz-(z**j)/fatorial(j)
        else:
            cosz=cosz+(z**j)/fatorial(j)
        iesimo=valor_absoluto((z**j)/fatorial(j))
        j=j+2
        i=i+1
    return cosz

def razao_aurea(m,epsilon):
    r=2*cosseno(pi(m)/5,epsilon)
    return r
            