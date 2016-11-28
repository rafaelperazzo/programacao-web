# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

#ÁREA DESTINADA AO CALCULO DAS FUNÇÕES QUE FAZEM-SE NECESSÁIAS PARA O FUNCIONAMNETO DO PROGRAMA. 






#função onde o objetivo principal é encontrar o valor absoluto do x, ou seja, o modulo do número. Como é extritamente proibido o uso de bibliotecas que facilitem o calculo do seu módulo(valor absoluto), usamo essa função para calcular.
#se o x(número) for negativo, multiplica-se ele por -1, e retorna o valor obtido(x), caso contrário, apenas retorna o valor(x).


def calcula_valor_absoluto(x):
    if x<0:
        x=x*(-1)
        return x
    else:
        return x



#FUNÇÃO DESTINADA AO CÁLCULO DO PI, ONDE ELE VAI SER INSERIDO UM PARAMETRO (M), E APARTIR DAI SERÁ CALCULADO O SEU VALOR(PI).
#COMO EXISTE UMA CONDIÇÃO DO M, ELE TEM QUE SER 1<=M<=2000, TEM QUE ESTAR ENTRE ESSES VALORES, USAMOS A CONDIÇÃO WHILE PARA COLOCAR ESSA CONDIÇÃO.
#DEPOIS APLICA-SE A FORMULA DO PI.
#COMO DETALHADO NA FORMULA, PERCEBE-SE QUE OS TERMOS DE NÚMERO ÍMPAR PRECEDEM DE UM -, E OS PARES DE +, CONSTATANDO ISSO, PODEMOS CRIAR UMA CONDIÇÃO, QUE CONSIGA SATISFAZER ESSE SEQUENCIA.
#NA FORMULA O VALOR DE PI, JÁ INICIA COM 3, QUE LOGO APÓS SERÁ SOMADO COM O RESULTADO DA SOMA.
#LOGO APÓS RETORNA-SE O VALOR DE PI.


def calcula_pi(m):
    soma=0
    i=1
    j=2
    while i<=m:
        if 1<=m and m<=2000:
            if i%2==0:
                soma=soma-(4/(j*(j+1)*(j+2)))
            else:
                soma=soma+(4/(j*(j+1)*(j+2)))
        i=i+1
        j=j+2
    pi=3+soma
    return pi

 
#...

def fatorial(a):
    fatorial=1
    for i in range(1,a,1):
        fatorial=fatorail*i
        
    return fatorial



#...

def calcula_co_seno(z,e):
    i=1
    j=2
    soma=0
    termo=((z**j)/fatorial(j))
    while termo>e:
        if i%2!=0:
            soma=soma-termo
        else:
            soma=soma+termo
        
        i=i+1
        j=j+2
        termo=((z**j)/fatorial(j))
        
    cos=1+soma
    return cos

#...

def calcula_razao_aurea(m,e):
    formula=calcula_co_seno((calcula_pi(m)/5.0,e))
    razao_aurea=2*formula
    
    return razao_aurea