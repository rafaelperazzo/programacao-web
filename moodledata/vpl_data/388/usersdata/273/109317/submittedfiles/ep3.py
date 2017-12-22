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


epsilon=float(input('Digite o valor de epsilon: '))
n=1
a=1
b=(1/(2**0.5))
resultado=0
while(abs(a-b))>epsilon:
    mediaa=((a+b)/2)
    mediag=((a*b)**0.5)
    c=((mediaa**2)-(mediag**2))
    
    resultado=resultado+(2**(n+1)*c)
    n=n+1
    a=mediaa
    b=mediag

pi=(4*(mediaa**2))/(1-resultado)
print(pi)


    