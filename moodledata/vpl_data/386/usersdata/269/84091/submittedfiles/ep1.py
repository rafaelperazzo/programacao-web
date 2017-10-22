# -*- coding: utf-8 -*-
''' Equipe: David Willian Gonçalves Silveira e Maria Luana Bezerra de Lima '''
''' Número de matriculAS: 405389 E 405958 '''
''' Exercicio-Programa 1 -- Raízes de Equações Quadráticas '''
''' ECI0007 (EC) -- 2017 -- Professor: Rafael Perazzo '''
''' Interpretador: Python versão 3 '''

import math 
a=int(input('digite a: '))
if a!=0:
    b=int(input('digite b: '))
    c=int(input('digite c: '))
    delta=(b*b)-(4*a*c)
    if delta==0:
        x1= (-1*b)/2*a
        x2= x1
        print('real dupla')
        print(x1)
        print(x2)
    if delta>0:
        epsilon=0.00000000001
        r0=delta
        r1=(delta+(delta/delta))/2
        if abs(r1-r0)<epsilon:
            delta=r1
        else:
        
            def raiz_quadrada(x, epsilon):
                rn=(rant+(x/rant))/2
            rant=r1
            
            while abs(rn-rant)>=epsilon:
                rant=rn
                def raiz_quadrada(delta, epsilon):
                    
        delta=rn        
                    
                
            
              
        
                







else:
    print('ERRO: equação não é do segundo grau')
