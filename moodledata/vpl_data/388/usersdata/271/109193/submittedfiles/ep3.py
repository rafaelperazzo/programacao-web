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
a = 1
b = 1/((2)**0.5)

precisao = float (input('Digite a precisão: '))

#FUNÇÃOARITMÉTICA-G
def arit (a,b):
    arit = (a + b)/2
    return(arit)
    
def geo (a,b):
    geo = (a*b)**(1/2)
    return (geo)
    
n = 1
soma = 0
acopia = a
bcopia = b

while abs (a-b)>precisao:
    a1 = arit (a,b)
    b1 = geo (a,b)
    c = (a1*a1) - (b1*b1)
    soma = soma + (2**(n+1))*c

    n = n + 1
    a = a1
    b = b1

pi = (4*(arit(a1,b1)))/(1-soma)
print (pi)