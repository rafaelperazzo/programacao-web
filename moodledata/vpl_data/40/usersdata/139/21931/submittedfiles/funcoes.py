#ARQUIVO COM SUAS FUNCOES
from__future__ import division 

def calcula_pi (m):
    i=1
    j=0
    a=2
    while i<=m:
        if l<=m<=2000:
            if i%2==0:
                j=j-(4/(a*(a+1)*(a+2)))
            else:
                j=j+(4/(a*(a+1)*(a+2)))
        i=i+1
        a=a+2
    pi=3+j
    return pi
def calcula_valor_absoluto(x):
    if x<0:
        x=x*(-1)
        return x
    else:
        return x
def fatorial(x):
    fatorail=1
    i=1
    while i<=x:
        fatorial=fatorial*i
        i=i+1
    return fatorial
def calcula_co_sem(z,e):
    i=1
    b=2
    j=0
    termo=((z**b)/fatorial(b))
    while termo>e:
        termo=((z**b)/fatorial(b))
        if i%2!=0:
            j=j-termo
        else:
            j=j+termo
        i=i+1
        b=b+2
    cos=1+j
    return cos
def calcula_razao_aure(m,e):
    i=calcula_co_sen((calcula_pi(m))/5,e)
    razao_aurea=2*i
    return razao_aurea