# -*- coding: utf-8 -*-
'''
/**********************************************************/
/* Equipe:  Andtalys Lauriano e Daniel Apolinario         */
/* Ńumero de matriculas:407549, 405947                    */
/* Exercicio-Programa 2 -- TEMA                           */
/* ECI0007 ou EM0006 (EC/EM) -- 2017 -- Professor: Rafael Perazzo      */
/* Interpretador: Python vers~ao 3                            */
/**********************************************************
'''


#COMECE SEU CODIGO NA LINHA ABAIXO.
#FUNÇÕES:
#*** PI ***#
def pi(m):
    pi=3
    a=2
    for i in range (1,m+1,1):
        if i%2!=0:
            pi=pi+(4/(a*(a+1)*(a+2)))
        else:
            pi=pi-(4/(a*(a+1)*(a+2)))
        a=a+2
    return (pi)