# -*- coding: utf-8 -*-
'''
/**********************************************************/
/* Equipe: Igor Emanuel e Victória Cruz                                  */
/* N ́umero de matriculas:.                    */
/* Exercicio-Programa 2 -- TEMA */
/* ECI0007 ou EM0006 (EC/EM) -- 2017 -- Professor:  */
/* Interpretador: Python vers~ao 3                            */
/**********************************************************
'''
#COMECE SEU CODIGO NA LINHA ABAIXO.
def valorabsoluto(x):
    if x<0:
        return (x*(-1))
    else:
        return(x)
        
def numpi(m):
    n=2
    pi=0
    for termo in range(1,m+1,1):
        if termo%2==0:
            pi=pi-(4/n*(n+1)*(n+2))
        else:
            pi=pi+(4/n*(n+1)*(n+2))
            
        n=n+3
        return(pi)
        
m=int(input('Digite m: '))
print(numpi(m))