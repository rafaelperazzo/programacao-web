#ARQUIVO COM SUAS FUNCOES
from __future__ import division
def calcula_valor_absoluto(x):
    if x<0:
        x=-x
    return x

def calcula_pi(m):
    m= calcula_valor_absoluto(m)
    cont=1
    pi=3
    i=3
    while cont<=m:
        valor= 4/((i-1)*(i)*(i+1))
        cont=cont+1
        if cont%2==0:
            pi=pi+valor
        else:
            pi=pi-valor
        i=i+2
    return pi
    
def fatorial(v):
    produto=1
    for i in range(1,v+1,1):
        produto=produto*i
    return produto

def calcula_co_seno(z,epsilon):
    cont=0
    cosseno=1
    i=2
    quociente=1
    while True:
        quociente= (z**i)/fatorial(i)
        cont=cont+1
        if quociente<epsilon:
            break
        else:
            if cont%2!=0:
                cosseno=cosseno-quociente
            else:
                cosseno=cosseno+quociente
        i=i+2
    return cosseno

def calcula_razao_aurea(m,epsilon):
    z= calcula_pi(m)/5
    fi=2*(calcula_co_seno(z,epsilon))
    return fi