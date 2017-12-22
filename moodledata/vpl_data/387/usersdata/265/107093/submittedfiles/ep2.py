# -*- coding: utf-8 -*-
'''
Equipe: Aurélio Bneto do Nascimento, Aparecido Petrison Belém Batista
Ńumero de matriculas:405386,405944
Exercicio-Programa 2 -- TEMA
ECI0007 ou EM0006 (EC/EM) -- 2017 -- Professor: Rafael Perazzo
Interpretador: Python vers~ao 3
/**********************************************************
'''
#COMECE SEU CODIGO NA LINHA ABAIXO.
def valorabsoluto(a):
    if a>=0:
        a=a
    if a<0:
        a=-a
    return(x)
    
def pi(b):
    soma=3
    num=4
    den1=2
    den2=3
    den3=4
    termo=0
    cont=0
    while cont<m:
        if ((termo%2)==0):
            soma=soma+num/(den1*den2*den3)
        else:
            soma=soma-num/(den1*den2*den3)
        den1=den1+2
        den2=den2+2
        den3=den3+2
        cont=cont+1
        termo=termo+1
    return(soma)
def fatorial(c):
    fator=1
    while c>0:
        fator=fator*y
        y=y-1
    return(fator)
def co_seno(d,epsilon):
    soma=1
    cont=0
    i=2
    termo=1
    while termo>=epsilon:
        if cont%2==0:
            soma=soma-((z**i)/fatorial(i))
        else:
            soma=soma+((z**i)/fatorial(i))
        i=i+2
        cont=cont+1
        termo=valorabsoluto((z**i)/fatorial(i))
    return(soma)
def razaoaurea(m,epsilon):
    phi=2*(co_seno(((pi(m))/5),epsilon))
    return(phi)
m=int(input('digite o numero m de termos da formula de pi: '))
epsilon=float(input('digite o valor de epsilon para o calculo da raza aurea: '))
print('%.15f' %pi(m))
print('%.15f' %razaoaurea(m,epsilon))