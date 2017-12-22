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
    pi=3
    for termo in range(1,m+1,1):
        if termo%2==0:
            pi=pi-(4/(n*(n+1)*(n+2)))
        else:
            pi=pi+(4/(n*(n+1)*(n+2)))
            
        n=n+2
    return('%.15f' %pi)
        
def fatorial(a):
    fator=1
    while(a>0):
        fator=fator*a
        a=a-1
    return(fator)
        
def cos(z,epsilon):
    n=2
    cosseno=0
    termo=2
    while(cosseno<epsilon+1):
        if termo%2!=0:
            cosseno=cosseno+((z**n)/fatorial(n))
        else:
            cosseno=cosseno-((z**n)/fatorial(n))
        n=n+2
        termo=termo+1
    cosseno=cosseno-1
    
        
    return(cosseno)
    
    
z=int(input('digite z: '))
epsilon=float(input('epsilon: '))
print(cos(z,epsilon))
            

    