# -*- coding: utf-8 -*-
'''
/********************************************************************************/
/* Equipe : Felipe Tavares de Menezes Pereira e Vitória Tiffany Teixeira Braga  */
/* Numeros de Matriculas : 405949 e 405410                                      */
/* Exercicio-Programa 1 -- Raizes de Equações Quadráticas                       */
/* ECI0007(T2) -- 2017 -- Professor : Rafael Perazzo                            */
/* Interpretador: Python versão 3                                               */
/********************************************************************************/
'''
#ENTRADA
n = int(input('Digite a quantidade de equacoes : '))
eps = float(input('Digite o valor da precisao : '))

#PROCESSAMENTO

def raiz(x,eps) :
    r0 = x
    r1 = (1/2) * (r0+(x/r0))
    while abs(r1-r0)<eps :
        r0 = r1
        r1 = (1/2) * (r0+(x/r0))
    return(r1)
    
raiz (n,eps)

print(r1)
    