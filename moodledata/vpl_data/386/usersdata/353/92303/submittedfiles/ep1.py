# -*- coding: utf-8 -*-
'''
/**********************************************************/
/* Equipe: Igor Emanuel Lucas Farias, Victória Cruz Gouveia                                  */
/* N ́umero de matriculas: 407553, 407582                    */
/* Exercicio-Programa 1 -- Ra ́ızes de Equa ̧c~oes Quadr ́aticas */
/* ECI0007 ou EM0006 (EC/EM) -- 2017 -- Professor:Rafael  */
/* Interpretador: Python vers~ao 3                            */
/**********************************************************
'''
#COMECE SEU CODIGO NA LINHA ABAIXO.
def raiz2(x,epsilon):
    rn=x
    while True:
        rm=(1/2)*(rn + (x/rn))
        if abs (rm-rn)<epsilon:
            return(rm)
        rn=rm
 
def baskara(a,b,c):
    delta=(b**2) - 4*a*c
    if delta>=0:
        x1=((-b)+(raiz2(delta,epsilon)))/(2*a)
        x2=((-b)-(raiz2(delta,epsilon)))/(2*a)
        if delta>0:
            return('reais simples', x1, x2)
        elif delta==0:
            return('real dupla', x1, x2)
    else:
        delta=delta*(-1)
        x3=((raiz2(delta,epsilon))/(2*a))       
        x1=((-b)/(2*a))
        x2=((-b)/(2*a))
        return('complexas', ('%x + %x i'%(x1,x2)), ('%x - %x i'%(x2,x3)))
        
   
    
epsilon=float(input('Digite o epsilon de controle: '))
nequacoes=int(input('Digite o número de equações: '))

for equação in range(0,nequacoes,1):
    a=float(input('Digite o a da equação: '))
    b=float(input('Digite o b da equação: '))
    c=float(input('Digite o c da equação: '))
    
    if a!=0:
        print(a), print(b), print(c), print(baskara(a,b,c))
    else:
        print('***ERRO: equação não é do segundo grau! ***')