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
#INICIALMENTE DEFINIREMOS AS FUNÇÕES NECESSARIAS PARA SOLUCIONAR O PROBLEMA

'''DEFININDO A FUNÇÃO PARA CALCULAR A RAIZ QUADRADA'''
def raiz_quadrada (x,epsilon):
    ratual=x
    while True :
        rproximo = (1/2)*(ratual+(x/ratual))
        if abs (rproximo-ratual)<epsilon:
            return (rproximo)
        ratual=rproximo

'''DEFININDO A FUNÇÃO PARA CALCULAR O VALOR DO DELTA'''
def delta(a,b,c):
    delta=(b**2)-(4*a*c)
    return(delta)

'''DEFININDO A FUNÇÃO PARA CALCULAR O VALOR DAS RAIZES ,USANDO O MÉTODO DE BASKARA'''
def raizes (a,b,c,delta):
    if (delta==0):
        raiz1=(-b/(2*a))
        return('raiz dupla','%.5f' % raiz1)
        
    elif(delta)>0:
        raiz1= (-b/2*a)+((raiz_quadrada(delta,epsilon))/2)
        raiz2= (-b/2*a)-((raiz_quadrada(delta,epsilon))/2)
        return('real simples','%.5f'% raiz1,'%.5f'% raiz2)
    else:
        real= (-b/2*a)
        delta= -delta
        complexa1= (+1)*(raiz_quadrada(delta,epsilon))/2*a
        complexa2= (-1)*(raiz_quadrada(delta,epsilon))/2*a
        return('complexas','%.5f'%real ,'+i*','%.5f'%complexa1,'%.5f'%real,'+i*','%.5f'%complexa2)

'''APÓS AS FUNÇÕES ESTAREM DEFINIDAS, PEDIREMOS OS DADOS DE ENTRADA'''
a=float(input('Digite o valor de a: '))
b=float(input('Digite o valor de b: '))
c=float(input('Digite o valor de c: '))
epsilon=float(input('Digite o valor de epsilon: '))

'''IREMOS PARA O PROCESSAMENTO E LOGO EM SEGUIDA JÁ MOSTRAREMOS OS DADOS DE SAÍDA'''
delta=delta(a,b,c)
k=raizes(a,b,c,delta)
if (a==0):
    print('***ERRO: equação não é do segundo grau!*** ')
else:
    print(a,b,c,k)
    

    


        

        
    
            
        
        
        
    
    