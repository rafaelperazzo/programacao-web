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
a=1
b=1/(2**0.5)
e=0.00000000001

soma=0

while (a-b)>e:
    ari=(a+b)/2
    geo=(a*b)**(0.5)
    c=(ari**2)-(geo**2)
    soma=soma+((2**(x+1))*c
    x=x+1
    a=ari
    b=geo
    
pi=(4*(a**2))/(1-soma)
print(pi)