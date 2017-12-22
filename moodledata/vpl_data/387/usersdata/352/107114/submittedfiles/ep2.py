# -*- coding: utf-8 -*-
'''
/**********************************************************/
/* Equipe: Andtalys Lauriano, Daniel Aplolinario          */
/* Número de matrículas: 407549,405947                   */
/* Exercicio-Programa 2 -- Razão Aurea                    */
/* ECI0007 (EC) -- 2017 -- Professor: Rafael Perazzo      */
/* Interpretador: Python versão 3                         */
/**********************************************************
'''
#COMECE SEU CODIGO NA LINHA ABAIXO.

#Funções

#**Valor Absoluto**#
def absoluto(x):
    if (x<0):
        x=-1*x
    else:
        x=x
    return(x)
    

#**PI**#
def def_pi(m):
    pi=3
    a=2
    for i in range (1,m+1,1):
        if i%2!=0:
            pi=pi+(4/(a*(a+1)*(a+2)))
        else:
            pi=pi-(4/(a*(a+1)*(a+2)))
        a=a+2
    return(pi)
    
#***Cosseno**#
def cos(x,e):
    cosx=1
    i=2
    fat=1
    cont=1
    while True:
        fat=fat*(i-1)*1
        if cont%2==0:
            cosx=cosx+((x**1)/fat)
        else:
            cosx=cosx-((x**1)/fat)
        if (((x**i)/fat)<=e):
            break
        cont=cont+1
        i=i+2
    return (cosx)

#Programa Principal
m=0
epsilon=0
while (m>=1 or m<=2000):
    m=int(input('Digite o numero m termos da formula de pi: '))
while (epsilon<=0 or epsilon>=1):
    epsilon=float(input('Digite o epsilon para o cálculo da razao aurea: '))
pi=def_pi(m)
x=pi/5
cosseno=cos(x,epsilon)
aurea=2*cosseno
print('Valor aproximado de pi:' '%.15f' %pi)
print('Valor aproximado da razao aurea:%.15f' %aurea)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    