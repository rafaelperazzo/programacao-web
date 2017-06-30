# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
def calcula_valor_absoluto(x):
    if x<0:
        x=x*(-1)
        return x
    else: 
        return x
def calcula_pi(m):
    a=2
    b=3
    c=4
    soma=3
    for i in range(0,m,1):
        if i%2==0:
            soma=soma+4/(a*b*c)
            else:
                soma=soma-4/(a*b*c)
        a=a+2
        b=b+2
        c=c+2
    return soma
def calcula_co_seno(z,epsilon):
    produtodosfatoriais=1
    soma=1
    a=2
    b=1
    expoente=2
    termo=2
    while(z**expoente/produtodosfatoriais)>=epsilon:
        fatorialatual=a*b
        produtodosfatoriais=produtodosfatoriais*fatorialatual
        if termo%2==0:
            soma=soma-(z**expoente/produtodosfatoriais)
        else:
            soma=soma+(z**expoente/produtodosfatoriais)
        termo=termo+1
        a=a+2
        b=b+2
        expoente=expoente+2
    cosseno=soma
    return cosseno
def calcula_razao_aurea(m):
    razaoaurea=2*m
    return razaoaurea

a=int(input('n de termo da formula pi: '))
epsilon=float(input('Digite o epsilon: '))
pi=calcula_pi(a)
modulodepi=calcula_valor_absoluto(pi)
pisobrecinco=modulodepi/5
cosseno=calcula_co_seno(pisobrecinco,epsilon)
razao=calcula_razao_aurea(cosseno)
print('%.15f'%modulodepi)
print('%.15f'%razao)