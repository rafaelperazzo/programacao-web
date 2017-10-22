# -*- coding: utf-8 -*-

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
cont=0

while(cont<n):
    
    #ENTRADA
    
    a=float(input('Digite o valor de a: '))
    b=float(input('Digite o valor de b: '))
    c=float(input('Digite o valor de c: '))
    epsilon=float(input('Digite a precisão das raízes: '))
    
    #PRE-ENTRADA
    
    if (a==0):
        print('ERRO: equação não é do segundo grau!')
    if (a!=0):
        Delta=((b**2)-4*a*c)
        
    #PROCESSAMENTO
    
        if (Delta>=0):
            Raiz= raiz_quadrada(Delta,epsilon)
            
            X1=(b-Raiz)/(2*a)
            X2=(b+Raiz)/(2*a)
            
            if (X1==X2):
                print('real dupla')
                print(X1)
                print(X2)
            if (X1!=X2):
                print('reais simples')
                print(X1)
                print(X2)
                
        if (Delta<0):
            Delta=-Delta
            Complexo= raiz_quadrada(Delta,epsilon)
            
            X1= (b)/(2*a)
            X2= (b)/(2*a)
            
            Complexo_1= -Complexo/(2*a)
            Complexo_2= Complexo/(2*a)
            
            print('complexas')
            print(' %f + i*%f' %(X1,Complexo_1))
            print(' %f + i*%f' %(X2,Complexo_2))
            
        
    