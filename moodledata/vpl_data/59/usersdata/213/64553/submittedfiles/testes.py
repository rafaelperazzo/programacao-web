# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
def calcula_pi(m):
    pi=3
    x=2
    for i in range(1,m+1,1):
        if i%2==0:
            pi=pi-((4)/(x*(x+1)*(x+2)))
        else:
            pi=pi-((4)/(x*(x+1)*(x+2)))
        x=x+2
    return(pi)

def calcula_fatorial(denominador2):
    i=1
    fatorial=1
    while i<=denominador2:
        fatorial=fatorial*i
        i=i+1
    return(fatorial)

def calcula_co_seno(z,epsilon):
    valorCosseno=1
    denominador1=2
    denominador2==calcula_fatorial(2)
    i=1
    while ((z**denominador1)/(denominador2) >= epsilon:
        if i%2==0:
            valorCosseno=valorCosseno+((z**denominador1)/(denominador2==calcula_fatorial(denominador2)))
        else:
            valorCosseno=valorCosseno-((z**denominador1)/(denominador2==calcula_fatorial(denominador2)))
        i=i+1
        denominador1=denominador1+2
        denominador2=calcula_fatorial(denominador1)
    return(valorCosseno)

def razao_aurea(valorCosseno):
    razaoAurea=2*(valorCosseno)
    return(razaoAurea)

m=int(input('Digite o numero m de termos da formula pi: '))
epsilon=float(input('Digite o epsilon para o calculo da Razao Aurea: '))

pi=calcula_pi(m)
z=(pi/5)
valorCosseno=calcula_co_seno(z,epsilon)
razao_aurea=razao_aurea(valorCosseno)

print('Valor aproximado de pi: %.15f' %pi)
print('Valor aproximado da razao aurea: %.15f' %razao_aurea)
