# -*- coding: utf-8 -*-
'''
/********************************************************************************/
/* Equipe: Felipe Tavares de Menezes Pereira e Vitória Tiffany Teixeira Braga   */
/* N ́umero de matriculas :405949 e 405410                                       */
/* Exercicio-Programa 2 -- Razão Áurea                                          */
/* ECI0007 (EC) Turma 2 -- 2017 -- Professor: Rafael Perazzo                    */
/* Interpretador: Python vers~ao 3                                              */
/********************************************************************************/
'''
#COMECE SEU CODIGO NA LINHA ABAIXO.
#ENTRADA
x = float(input('Digite o valor de x : '))
eps = float(input('Digite o erro : '))

#PROCESSAMENTO
def fatorial (n):
    mult = 1
    while (mult<=n) :
        fatorial = (mult*(mult+1))
        mult = mult+1
    return (fatorial)
    
print(fatorial (x))