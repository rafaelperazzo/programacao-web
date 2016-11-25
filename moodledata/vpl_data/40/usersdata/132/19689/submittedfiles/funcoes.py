# -*- coding: utf-8 -*-
#ARQUIVO COM SUAS FUNCOES
from __future__ import division
def pi(x):#Criação da função que calcula o valor de pi
    s=3
    a=0
    i1=2
    i2=3
    i3=4
    while(a<x):#Repetição com sua condição de parada
        y=((4)/(i1*i2*i3))
        if (i3)%4==0:#condição para a soma, o contrário é a condição para subtrair
            s=s+y
        else:
            s=s-y
        i1=i1+2#atualização
        i2=i2+2#atualização
        i3=i3+2#atualização
        a=a+1#atualização
    return s# Variável a ser retornada   
def modulo(x):#Criação da função que calcula o módulo
    if x<0:
        x=x*-1
        return x
    else:
        return x
def cos(z,e):#Criação da função que calcula o valor do co-seno
    s=1
    e=modulo(e)
    cont=1
    n=2
    while True:
        fatorial=1
        for i in range(1,n+1,1):
            fatorial=fatorial*i
        y=(z**n)/fatorial
        if y<e:
            break
        if cont%2!=0:
            y=y*-1
        s=s+y
        n=n+2
        cont=cont+1
    return s    
def aurea(m,e):#Criação da função que calcula o valor da razão áurea
    x=2*cos(pi(m)/5,e)
    return x