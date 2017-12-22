# -*- coding: utf-8 -*-
'''
/**********************************************************/
/* Equipe: Vitória Tiffany Teixeira Braga,Felipe Tavares de Menezes Pereira                              */
/* Ńumero de matriculas:405410,405949.                    */
/* Exercicio - Programa 3 -- TEMA */
/* ECI0007 (T2) -- 2017 -- Professor:  Rafael Perazzo
/* Interpretador: Python vers~ao 3                            */
/**********************************************************
'''
#COMECE SEU CODIGO NA LINHA ABAIXO.
a = float (input('Digite o valor de a: '))
b = float (input('Digite o valor de b: '))
precisao = float (input('Digite a precisão: '))

#FUNÇÃOARITMÉTICA-G
def aritgeo (a,b,precisao) :
    aritmetica = 0
    geometrica = 0
    while ((a-b)>precisao) and (a>b) :
        a1 = (1/2)*(a+b)
        b1 = (a*b)**(0.5)
        aritmetica = aritmetica + a1
        geometrica = geometrica + b1
        a = a1
        b = b1
        
        
