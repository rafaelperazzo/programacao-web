# -*- coding: utf-8 -*-
'''
/**********************************************************/
/* Equipe: Fulano de Tal                                  */
/* N ́umero de matriculas: 12345678, ...                    */
/* Exercicio-Programa 2 -- TEMA */
/* ECI0007 ou EM0006 (EC/EM) -- 2017 -- Professor:  */
/* Interpretador: Python vers~ao 3                            */
/**********************************************************
'''
#COMECE SEU CODIGO NA LINHA ABAIXO.

#FUNÇÕES

def calcula_valor_absoluto(x):
    if (x>=0):
        x=x
    elif (x<0):
        x=-x
    return(x)
    
def calcula_pi(m):
    
    soma=3
    num=4
    d1=2
    d2=3
    d3=4
    sinal_pi=0
    cont=0
    
    while(cont<m):
        
        if((sinal_pi%2)==0):
            soma = soma + num/(d1*d2*d3)
        if((sinal_pi%2)==1):
            soma= soma - num/(d1*d2*d3)
        
        d1=d1+2
        d2=d2+2
        d3=d3+2
        cont=cont+1
        sinal_pi= sinal_pi+1
        
    return(soma)

def calcula_fatorial(y):
    fatorial=1
    while(y>0):
        fatorial=fatorial*y
        y=y-1
    return(fatorial)
    
def calcula_co_seno(z,epsilon):
    soma=1
    cont=0
    i=2
    termo=1
    while (termo>=epsilon):
        if (cont%2==0):
            soma=soma - ((z**i)/calcula_fatorial(i))
        else:
            soma=soma + ((z**i)/calcula_fatorial(i))
    
        i=i+2
        cont=cont+1
        termo=calcula_valor_absoluto((z**i)/calcula_fatorial(i))
    
    return(soma)

def calcula_razao_aurea(m,epsilon):
   
    phi=2*(calcula_co_seno(((calcula_pi(m))/5),epsilon))
    return(phi)

m=int(input('Digite o numero m de termos da formula de pi: '))
epsilon=float(input('Digite o epsilon para o calculo da razao aurea: '))

print('Valor aproximado de pi: %.15f' %calcula_pi(m))
print('Valor aproximado da razao aurea: %.15f' %calcula_razao_aurea(m,epsilon))


    
    
        