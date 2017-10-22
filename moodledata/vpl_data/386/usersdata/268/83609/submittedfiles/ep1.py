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
        
        if (Delta>0):
            Raiz_1= raiz_quadrada(Delta,epsilon)
            
        
    