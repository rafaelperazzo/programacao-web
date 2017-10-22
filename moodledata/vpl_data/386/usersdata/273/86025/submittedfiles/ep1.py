# -*- coding: utf-8 -*-
'''
/**********************************************************/
/* Equipe: Leandro Pedro Freitas , Gustavo Henrique Lima de Alencar         */
/* N ́umero de matriculas: 381420                    */
/* Exercicio-Programa 1 -- Ra ́ızes de Equa ̧c~oes Quadr ́aticas */
/* ECI0007 ou EM0006 (EC/EM) -- 2017 -- Professor:  */
/* Interpretador: Python vers~ao 3                            */
/**********************************************************
'''
#COMECE SEU CODIGO NA LINHA ABAIXO.
def raiz_quadrada (x,epsilon):
    ratual=x
    while True :
        rproximo = (1/2)*(ratual+(x/ratual))
        if abs (rproximo-ratual)<epsilon:
            return (rproximo)
        ratual=rproximo
        
def delta(a,b,c):
    delta=(b**2)-(4*a*c)
    return(delta)

def raiz (a,b,c,delta):
    '''if (delta==0):
        raiz1=(-b/2*a)
        return('raiz dupla',raiz1)'''
        
    if (raiz_quadrada(delta))>0:
        raiz1= (-b/2*a)+((raiz_quadrada(delta))/2)
        raiz2= (-b/2*a)-((raiz_quadrada(delta))/2)
        return('real simples',raiz1,raiz2)
    '''else:
        raiz1=(-b/2*a)+((raiz_quadrada(delta)*i)/2)
        raiz2=(-b/2*a)-((raiz_quadrada(delta)*i)/2)
        return('raiz compleza',raiz1,raiz2)'''
        
a=int(input('digite o valor de a : '))
b=int(input('digite o valor de b : '))
c=int(input('digite o valor de c : '))

raiz_quadrada=raiz_quadrada(2,0.0001)
delta=delta(a,b,c)
k=raiz(a,b,c,delta)
print(k)

        

        
    
            
        
        
        
    
    