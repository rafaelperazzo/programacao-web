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
e=0.1
a=1
b=1/(2**0.5)
n=1
soma=0
c=(a**2)-(b**2)
ariti=(a+b)/2
while (a-b)>e:
    soma=soma+ ((2**(n+1))*c)
    n=n+1
    a=(a+b)/2
    b=(a*b)**0.5

pi= (4*(ariti**2))/(1-soma)
print(pi)

