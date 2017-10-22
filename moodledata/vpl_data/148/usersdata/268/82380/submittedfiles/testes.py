# -*- coding: utf-8 -*-
n = int(input('Digite o número d equações: '))
cont=0

while (cont<n):
  
    #ENTRADA
    
    a=float(input('Digite o valor de a: '))
    b=float(input('Digite o valor de b: '))
    c=float(input('Digite o valor de c: '))
    E=float(input('Digite a precisão das raízes: '))
    
    #PRE-ENTRADA
    
    if (a==0):
        print('ERRO: equação não é do segundo grau!'))
    if (a!=0):
        Delta=((b**2)-4*a*c)
        Raiz=
        X1= (b - Raiz)/(2*a)
        X2= (b + Raiz)/(2*a)
        
        #FILTRO DE SAIDA
        
        if(X1==X2):
            print('real dupla')
            print(X1)
            print(X2)
        if (complexo==0) and (X1==X2):
            print('reais simples'):
                print(X1)
                print(X2)
    cont=cont+1
            
    
