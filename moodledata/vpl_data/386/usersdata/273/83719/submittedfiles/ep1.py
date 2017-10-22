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
            
def delta (a,b,c,delta):
    if (def raiz_quadrada)==0:
        return (-b/a)
    elif (def raiz_quadrada)>0:
        raiz1= (-b/2a)+((def raiz_quadrada)/2)
        raiz2= (-b/2a)-((def raiz_quadrada)/2)
        return(raiz1)
        return(raiz2)
    else:
        raiz1=(-b/2a)+((def raiz_quadrada*i)/2)
        raiz2=(-b/2a)-((def raiz_quadrada*i)/2)
        return(raiz1)
        return(raiz2)
        
        
    
            
        
        
        
    
    