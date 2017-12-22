# -*- coding: utf-8 -*-
'''
/**********************************************************/
/* Equipe: Fulano de Tal:Leandro Pedro de Freitas e Gustavo henrique                               */
/* N ́umero de matriculas:381420 e                    */
/* Exercicio-Programa 2 -- TEMA *Razao aurea
/* ECI0007 ou EM0006 (EC/EM) -- 2017 -- Professor: Rafael perazzo */
/* Interpretador: Python vers~ao 3                            */
/**********************************************************
'''
#COMECE SEU CODIGO NA LINHA ABAIXO.

def calcula_valor_absoluto (x):
    x=((x**2)**0.5)

def calcula_pi(epsilon):
    for i in range(0,epsilon,1):
        pi0=0
        a=2
        b=3
        c=4
        if ((i%2)==0):
            pi=pi0-(4/(a*b*c))
        else:
            pi=pi0+(4/(a*b*c))
        a=a+2
        b=b+2
        c=c+2
    valordopi=pi+3
    return(valordopi)
    

print(calcula_pi(10000000))