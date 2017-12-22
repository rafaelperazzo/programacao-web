# -*- coding: utf-8 -*-
'''
/**********************************************************/
/* Equipe: Igor Farias, Victória cruz*/
/* N ́umero de matriculas: 407553,407582                    */
/* Exercicio-Programa 3 -- TEMA */
/* ECI0007 ou EM0006 (EC/EM) -- 2017 -- Professor: Rafael */
/* Interpretador: Python vers~ao 3                            */
/**********************************************************
'''
#COMECE SEU CODIGO NA LINHA ABAIXO.
def aritmetica(a,b,epsilon):
    mediaa=(a+b)/2
    return (mediaa)
    
def geometrica(a,b,epsilon):
    mediag=((a*b)**(0.5))
    return (mediag)
    
def somatorio(c,epsilon):
    soma2=0
    while(a-b>epsilon):
        soma=(2**(n+1))*c
        soma2=soma2+soma
    return (soma2)
    
def pi(aritmetica, somatorio):
    valorpi=(4*(aritmetica**(0.5)))/(1-somatorio)
    return(valorpi)


a=1
b=1/(2**(0.5))
n=1

epsilon=float(input('Digite a variavel de controle(epsilon): '))

while (a-b)>epsilon:
    a1=(aritmetica(a,b,epsilon))
    b1=(geometrica(a,b,epsilon))
    c=(a1**2)-(b1**2)
    soma=soma+ ((2**(n+1))*c)
    n=n+1
    a=a1
    b=b1

print(pi(a,soma))