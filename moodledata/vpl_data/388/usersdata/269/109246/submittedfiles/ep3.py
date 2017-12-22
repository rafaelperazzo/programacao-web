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
n=1
e=0.00000001
a=float(input('digite a: '))
b=float(input('digite b: '))
soma=0
while (a-b)>e:
    ariti=(a+b)/2
    geo=(a*b)**0.5
    c=(a**2)-(b**2)
    soma=soma+ (2**(n+1))*c
    n=n+1
    a=(a*b)**0.5
    b=(a+b)/2
    
pi= (4*(ariti**2))/(1-soma)
print(pi)