# -*- coding: utf-8 -*-
'''
/**********************************************************/
/* Equipe: Aurélio Bento do Nascimento, Aparecido Petrison Belém Batista */
/* N ́umero de matriculas: 405386,   */
/* Exercicio-Programa 3 -- TEMA */
/* ECI0007(EC) -- 2017 -- Professor: Rafael Perazzo */
/* Interpretador: Python vers~ao 3                            */
/**********************************************************
'''
#COMECE SEU CODIGO NA LINHA ABAIXO.
a=float(input('digite o valor de a: '))
b=float(input('digite o valor de b: '))
E=float(input('digite o vlor da precisão: '))
n=1
somatorio=0
while (a-b)>E:
    mediaAritmetica=(a+b)/2
    mediaGeometrica=(a*b)**0.5
    c=(a**2)-(b**2)
    somatorio=somatorio+(2**(n+1))*c
    n=n+1
    break
    

pi=(4*(mediaAritmetica**2))/(1-somatorio)
print(pi)