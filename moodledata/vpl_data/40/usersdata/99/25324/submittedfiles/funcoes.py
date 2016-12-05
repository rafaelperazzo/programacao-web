#ARQUIVO COM SUAS FUNCOES
from __future__ import division

def calcula_valor_absoluto(x):
    if x<0:
        x=x*(-1)
    else:
        x=x
    return x
    
def calcula_pi(m):
    i=1
    soma=0
    den=2
    if 1<=m<=2000:
        while i<=m:
            if i%2==0:
                soma=soma-(4/(den*(den+1)*(den+2)))
            else:
                soma=soma+(4/(den*(den+1)*(den+2)))
            i=i+1
            den=den+2
        pi=3+soma
        return pi

def fatorial(x):
    