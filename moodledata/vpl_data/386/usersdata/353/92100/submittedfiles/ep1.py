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
    for rn in range(0,epsilon,1):
        rm=(1/2)*(rn +(x/rn))

def baskara(a,b,c):
    delta=(b**2) - 4*a*c
    if delta>=0:
        x1=((-b)+(raiz2(delta,epsilon)))/(2*a)
        x2=((-b)-(raiz2(delta,epsilon)))/(2*a)
        if delta>0:
            return('reais simples')
            return(x1) 
            return(x2)
        elif delta==0:
            return('real dupla')
            return(x1)
            return(x2)
    else:
        x3=((raiz2(-delta,epsilon))/(2*a))       
        x1=((-b)/(2*a))
        x2=((-b)/(2*a))
        return('complexas')
        return('%f+%f i'%(x1,x3))
        return('%f-%f i'%(x2,x3))
   
        
   
    
epsilon= float(input('Digite o epsilon: '))
nequacoes=int(input('Digite o número de equações: '))

for equação in range(0,nequacoes,1):
    a=float(input('Digite o a da equação: '))
    b=float(input('Digite o b da equação: '))
    c=float(input('Digite o c da equação: '))
    
    if a!=0:
        baskara(a,b,c)
        if delta>0:
            print(a), print(b), print(c), print('reais simples'), print(x1), print(x2)
        elif delta==0:
            print(a), print(b), print(c), print('real dupla'), print(x1), print(x2)
        else:
            print(a), print(b), print(c), print('complexas'), print(x1), print(x2)
    else:
        print('***ERRO: equação não é do segundo grau! ***')