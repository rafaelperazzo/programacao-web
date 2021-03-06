# -*- coding: utf-8 -*-
'''
/********************************************************/
/*Equipe: Davi N. de Freitas e José Matheus S. Pereira  */
/*Número de matrícula: 405388, 405399                   */
/*Exercício-Programa 1 -- Raízes de Equações Quadráticas*/
/*ECI007 (EC) -- 2017 -- Professor: Rafael              */
/*Interpretador:Python versão 3                             */
/********************************************************/
'''
#FUNÇAO

def raiz_quadrada(x,epsilon):
    r=x
    while True:
        rq=(1/2)*(r+(x/r))
        if (abs(r-rq)<epsilon):
            return(rq)
        r=rq
        
#INICIO

n= int(input('Digite o numero de equações: '))
epsilon=float(input('Digite a precisão das raízes: '))
cont=0

while(cont<n):
    
    #ENTRADA
    
    a=float(input('Digite o valor de a: '))
    b=float(input('Digite o valor de b: '))
    c=float(input('Digite o valor de c: '))
    
    
    #PRE-ENTRADA
    
    if (a==0):
        print('ERRO: equação não é do segundo grau!')
    if (a!=0):
        Delta=((b**2)-4*a*c)
        
    #PROCESSAMENTO
    
        if (Delta>0):
            
             Raiz= raiz_quadrada(Delta,epsilon)
              
             X1=(-b-Raiz)/(2*a)
             X2=(-b+Raiz)/(2*a)
           
             if (X1!=X2):
                 print('reais simples')
                 print('O valor de a é %f'%a)
                 print('O valor de b é %f'%b)
                 print('O valor de c é %f'%c)
                 print('%.5f'%X1)
                 print('%.5f'%X2)
       
        if (Delta==0):
            
             Raiz=0
             X1=(-b-Raiz)/(2*a)
             X2=(-b+Raiz)/(2*a)
            
             if (X1==X2):
                 print('real dupla')
                 print('%.5f'%X1)
                 print('%.5f'%X2)
            
                
        if (Delta<0):
            Delta=-Delta
            Complexo= raiz_quadrada(Delta,epsilon)
            
            X1= (-b)/(2*a)
            X2= (-b)/(2*a)
            
            Complexo_1= -Complexo/(2*a)
            Complexo_2= Complexo/(2*a)
            
            print('complexas')
            print(' %.5f + ( %.5f *i )' %(X1,Complexo_1))
            print(' %.5f + ( %.5f *i )' %(X2,Complexo_2))
            
        
    