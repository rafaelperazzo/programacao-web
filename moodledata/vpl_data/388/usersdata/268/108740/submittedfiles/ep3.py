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
a=float(input('Digite o primeiro valor: '))
b=float(input('Digite o segundo valor: '))
while(a<=b):
    a=float(input('Digite o primeiro valor: '))
    b=float(input('Digite o segundo valor: '))
epsilon=float(input('Digite o valor da precisão: '))

n=1
soma=0

while((a-b)>epsilon):
    aritmetica=(a+b)/2
    geometrica=(a*b)**(1/2)
    c=(a**2)-(b**2)
    soma=soma+(c*(2**(n+1)))
Passo4=soma
pi=(4*(aritmetica**2))/(1-Passo4)

print('O valor de pi é %f' %pi)
    
    
    
    
    
    
    
    

