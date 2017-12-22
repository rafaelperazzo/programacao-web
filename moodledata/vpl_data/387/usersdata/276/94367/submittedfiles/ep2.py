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
m = float(input('Digite o m : '))
eps = float(input('Digite o erro : '))

#FUNÇÕES
#FUNÇÃO VALOR ABSOLUTO
def calcula_valor_absoluto (x):
    if (x>=0):
        valor_absoluto = x
    else:
        valor_absoluto = -x
    return (valor_absoluto)

#FUNÇÃOPI
def calcula_pi (m):
    
    pi = 3
    posicao = 1
    i = 2
    
    while (posicao<=m):
        
        termo = 4/(i*(i + 1)*(i + 2))
    
        if (posicao%2 != 0):
            pi = pi + termo
            
        else:
            pi = pi - termo
            
        posicao = posicao + 1
        i = i + 2
        
    return (pi)

#FUNÇÃOFATORIAL
def fatorial (n):
    
    mult = 1
    fatorial = 1
    
    while (mult<=n) :
        fatorial = fatorial*mult
        mult = mult+1
    
    return (fatorial)

#FUNÇÃOCOS
def calcula_co_seno (z,eps):
    i = 2
    posicao = 1
    cos = 1
    num = z**(i)
    den = (fatorial (i))
    termo = (num/den)
    valor_absoluto_termo = calcula_valor_absoluto (termo)
    
    while (valor_absoluto_termo<=eps):
        if (posicao%2 !=0):
            cos = cos - termo
        else:
            cos = cos + termo
        i = i+2
        posicao = posicao + 1
        
        num = z**(i)
        den = (fatorial (i))
        termo = (num/den)
        
        valor_absoluto_termo = calcula_valor_absoluto (termo)    
        
    return (cos)
    
def calcula_razao_aurea (m,eps):
    divisao = calcula_pi (m)/5
    cos = calcula_co_seno (divisao, eps)
    razao_aurea = 2*cos
    return (razao_aurea)

print (calcula_pi (m))    
print (calcula_razao_aurea (m,eps))
    
    

    