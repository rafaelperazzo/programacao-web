#ARQUIVO COM SUAS FUNCOES
from __future__ import division
def calcula_valor_absoluto(x):
    if x<0:
        x=x*(-1)
    else:
        x=x
    return x

def Calcula_pi(m):
    soma=0
    i=1
    den=2
    if m<=1 and m<=2000:
        while i<=m:
            if i%2!=0:
                soma=soma+(4/((den)*(den+1)*(den+2)))
            else:
                soma=soma-(4/((den)*(den+1)*(den+2)))
            i=i+1
            den=den+2
            
    pi=soma+3
    return pi
    

def fatorial(x):
    i=1
    fat=1
    while i<=x:
        fat=fat*i
        i=i+1
    return fat
    
def calcula_co_seno(z,epsilon):
    soma=0
    i=1
    exp=2
    a=((z**exp)/fatorial(exp))
    while a>epsilon:
        a=((z**exp)/fatorial(exp))
        if i%2==0:
            soma=soma+a
        else:
            soma=soma-a
        exp=exp+2
        i=i+1
    cosseno=1+soma
    return cosseno
    
def calcula_razao_aurea(m,epsilon):
    pi=calcula_pi(m)/5
    razao_aurea=2*calcula_co_seno(pi,epsilon)
    
    return razao_aurea