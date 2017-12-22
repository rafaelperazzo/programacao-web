# -*- coding: utf-8 -*-
'''
/**********************************************************/
/* Equipe: Fulano de Tal:Leandro Pedro de Freitas e Gustavo henrique                               */
/* N ́umero de matriculas:381420 e                    */
/* Exercicio-Programa 2 -- TEMA *Razao aurea
/* ECI0007 ou EM0006 (EC/EM) -- 2017 -- Professor: Rafael perazzo */
/* Interpretador: Python vers~ao 3                            */
/**********************************************************
'''
#COMECE SEU CODIGO NA LINHA ABAIXO.

def calcula_valor_absoluto (x):
    x=((x**2)**0.5)

def calcula_pi(m):
    for i in range(1,m,1):
        pi0=0
        a=2
        b=3
        c=4
        if ((i%2)==0):
            pi=pi0-(4/(a*b*c))
        else:
            pi=pi0+(4/(a*b*c))
        a=a+2
        b=b+2
        c=c+2
    valordopi=pi+3
    return(valordopi)
    
def calcula_co_seno(z):
    for z in range(1,z,1):
        a=2
        deno=2
        cosseno=0
        if (z%2)==0:
            while (deno>0):
                produto=((calcula_valor_absoluto)/(deno))
                deno=deno-1
            cosseno=cosseno-produto
        else:
            while (deno>0):
                produto=((calcula_valor_absoluto)/(deno))
                deno=deno-1
            cosseno=cosseno+produto
        deno=deno+2
        a=a+2
    cosseno_real=cosseno+1
    return(cosseno_real)
    
def calcula_razao_aurea(m):
    razao=2*(calcula_co_seno(calcula_pi(m)/(5)))
    return(razao)
    
x=int(input('Digite o valor de x: '))
m=int(input('Digite o numero de termos para calcular pi: '))
z=int(input('Digite o numero de termos para calcular o cosseno: '))

l=calcula_pi(100)
j=calcula_razao_aurea(m)
z=100
print(l)
print(j)
    

    
    
        


                
            
            
            
            
            
            
            
            
            