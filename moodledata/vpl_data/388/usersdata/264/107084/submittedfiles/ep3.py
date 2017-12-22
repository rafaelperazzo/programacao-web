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
a=float(input('digite o valor de a: '))
b=float(input('digite o valor de b: '))
E=float(input('digite o vlor da precisão: '))
n=1
while (a-b)>E:
    media_aritimetica=(a+b)/2
    media_geometrica=(a*b)**0.5
    c=(a**2)-(b**2)
    somatorio=(2**(n+1))*c
    n=n+1

pi=(4*(media_aritimetica**2))/(1-somatorio)
print(pi)