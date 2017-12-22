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

#FUNÇÃOMODULO
def modulo (x):
    if (x>=0):
        modulo = x
    else:
        modulo = -x
    return (modulo)

#FUNÇÃOPI
def pi(m):
    soma = 3
    posicao = 2
    i = 1
    termo = 4/((i + 1)*(i + 2)*(i + 3))
    if (posicao%2 ==0):
        soma = soma + termo
    else:
        soma = soma - termo
    posicao = posicao +1
    i = i + 2

#FUNÇÃOFATORIAL
def fatorial (n):
    mult = 1
    fatorial = 1
    while (mult<=n) :
        fatorial = fatorial*mult
        mult = mult+1
    return (fatorial)

#FUNÇÃOCOS
def cos (n):
    i = 2
    soma = 1
    num = 
    termo = (num/den)
    posicao = 1
     
    while (termo<=eps):
        
    