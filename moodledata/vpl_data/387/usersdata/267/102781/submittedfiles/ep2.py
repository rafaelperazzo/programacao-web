# -*- coding: utf-8 -*-
'''
/**********************************************************/
/* Equipe:  Andtalys Lauriano e Daniel Apolinario         */
/* Ńumero de matriculas:407549, 405947                    */
/* Exercicio-Programa 2 -- TEMA                           */
/* ECI0007 ou EM0006 (EC/EM) -- 2017 -- Professor: Rafael Perazzo */
/* Interpretador: Python vers~ao 3                            */
/**********************************************************
'''


#COMECE SEU CODIGO NA LINHA ABAIXO.
#FUNÇÕES:
#*** VALOR ABSOLUTO ***#
def absoluto(x):
    if (x<0):
        x=-1*x
    else:
        x=x
    return(x)


#*** PI ***#
def def_pi(m):
    pi=3
    a=2
    for i in range (1,m+1,1):
        if i%2!=0:
            pi=pi+(4/(a*(a+1)*(a+2)))
        else:
            pi=pi-(4/(a*(a+1)*(a+2)))
        a=a+2
    return (pi)


#*** COSSENO ***#
def cos(x,e):
    cosx=1
    i=2
    fat=1
    cont=1
    while (x**i/(i*(i-1))<=e):
        fat=fat*(i-1)*i
        if cont%2!=0:
            cosx=cosx-(x**i/fat)
        else:
            cosx=cosx+(x**i/fat)
        cont=cont+1
        i=i+2
    return (cosx)
    
#*** RAZÃO ÁUREA ***#
#def aurea(m,
    

#PROGRAMA PRINCIPAL
m=0
epsilon=0
while (epsilon<=0 or epsilon>=1):
    epsilon=float(input('Precisão para cálculo do cosseno: '))
while (m<1 or m>2000):
    m=int(input('Precisão para cálculo do PI: '))
pi=def_pi(m)

x=pi/5
cosseno=cos(x,epsilon)
print(cosseno)




