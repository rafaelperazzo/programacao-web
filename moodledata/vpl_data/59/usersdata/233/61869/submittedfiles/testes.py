# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
def calcula_valor_absoluto(x):
    if x<0:
        x=x*(-1)
        return x
    else:
        return x
#Comentários sobre a função(calcula_pi)
# É sabido que na fórmula para calcular pi, cada fator do denominador varia dem duas unidades de termo para termo. 
#Exemplo: Se no segundo termo, temos(4/2*3*4), no terceiro, teremos(4/4*5*6). Para isso, chamaremos os fatores de a,b e c!
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
    
#Comentários sobre a função (calcula_cosseno)
#Sabemos no denominador desta fórmula, teremos o fatorial de um número que varia em duas unidades de termo para termo!
#Exemplo: /4!  , /6!
def calcula_cosseno(z,epsilon):
    produtodosfatoriais=1
    soma=1
    a=2
    b=1
    expoente=2
    termo=2
    while (z**expoente/produtodosfatoriais)>epsilon:
        fatorialatual=a*b
        produtodosfatoriais=produtodosfatoriais*fatorialatual
        if termo%2==0:
            soma=soma-(z**expoente)/produtodosfatoriais
        else:
            soma=soma+(z**expoente)/produtodosfatoriais
        termo=termo+1
        a=a+2
        b=b+2
        expoente=expoente+2
    cosseno=soma
    return cosseno
    
def calcula_razao_aurea(m):
    razaoaurea=2*m
    return razaoaurea
    
epsilon=float(input('Digite o epsilon: '))
a=int(input('Olá, querido amigo. Por favor, digite o número de termos da fórmula pi: '))
pi=calcula_pi(a)
modulodepi=calcula_valor_absoluto(pi)
pisobrecinco=modulodepi/5
cosseno=calcula_cosseno(pisobrecinco,epsilon)
modulodecosseno=calcula_valor_absoluto(cosseno)
razao=calcula_razao_aurea(modulodecosseno)
print('%.15f'%modulodepi)
print('%.15f'%razao)