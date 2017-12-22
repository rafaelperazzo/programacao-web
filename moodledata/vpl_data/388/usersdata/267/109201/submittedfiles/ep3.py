# -*- coding: utf-8 -*-
'''
/**********************************************************/
/* Equipe: Fulano de Tal                                  */
/* N ́umero de matriculas: 12345678, ...                    */
/* Exercicio-Programa 3 -- TEMA */
/* ECI0007 ou EM0006 (EC/EM) -- 2017 -- Professor:  */
/* Interpretador: Python vers~ao 3                            */
/**********************************************************
'''
#COMECE SEU CODIGO NA LINHA ABAIXO.
#a=float(input('Digite o valor do primeiro número: '))
#b=float(input('Digite o valor do segundo número: '))
a=1
b=1/2**0.5
while a<b:
    b=float(input('Digite o valor do segundo número (menor que o primeiro): '))
e=float(input('Digite a precisão: '))
n=1
while abs(a-b)>e:
    a=(a+b)/2
    b=(a*b)**0.5
    c=(a*a-b*b)
    soma=2**(n+1)*c
    n=n+1
pi=(4*a**2)/(1-soma)
print(pi)
    