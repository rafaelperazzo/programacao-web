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

def raiz(x,eps) :
    r0 = x
    r1 = (1/2) * (r0+(x/r0))
    while abs(r1-r0)>=eps :
        r0 = r1
        r1 = (1/2) * (r0+(x/r0))
    return(r1)

contador = 1
while (n>=contador):
    a = float(input('Digite o valor de a : '))
    b = float(input('Digite o valor de b : '))
    c = float(input('Digite o valor de c : '))
    
    if (a==0):
        print('*** ERRO: equação não é do segundo grau! ***')
        
    delta = (b*b) - (4*a*c)
    
    if (delta>0) :
        resposta_da_raiz = raiz(delta,eps)
        x1 = (-b + resposta_da_raiz)/(2*a)
        x2 = (-b - resposta_da_raiz)/(2*a)
        print('%.2f %.2f %.2f reais simples %.4f %.4f' % (a,b,c,x1,x2))
    
    elif (delta==0) :
        x = (-b)/(2*a)
        print('%.2f %.2f %.2f real dupla %.4f %.4f' % (a,b,c,x,x))
        
    else:
        delta = -delta
        resposta_da_raiz = raiz (delta,eps)
        x1_parte_real =(-b + resposta_da_raiz)/(2*a)
        x1_parte_imaginaria = 1/(2*a)
        x2_parte_real =(-b - resposta_da_raiz)/(2*a)
        print('%.2f %.2f %.2f complexas %.4f + %.4fi %.4f - %.4fi' % (a,b,c,x1_parte_real,x1_parte_imaginaria,x2_parte_real,x1_parte_imaginaria))
        
    contador = contador + 1
#PROCESSAMENTO


    