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
        x1= (-1*(b))/(2*a)
        x2= x1
        print('real dupla')
        print('%.4f' %x1)
        print('%.4f' %x2)
    if delta>0:
        epsilon=0.00000000001
        def raiz_quadrada(x, epsilon):
            rant=x
            rn=(rant+(x/rant))/2
            while abs(rn-rant)>= epsilon:
                rant=rn
                rn=(rant+(x/rant))/2
            return(rn)    
        raiz=raiz_quadrada(delta, epsilon)
        x1= ((-1*(b)) + raiz)/(2*a)
        x2= ((-1*(b)) - raiz)/(2*a)
        print('reais simples')
        print('%.4f' %x1)
        print('%.4f' %x2)
    
    if delta<0:
        delta=-1*delta
        epsilon=0.00000000001
        def raiz_quadrada(x, epsilon):
            rant=x
            rn=(rant+(x/rant))/2
            while abs(rn-rant)>= epsilon:
                rant=rn
                rn=(rant+(x/rant))/2
            return(rn)    
        raiz=raiz_quadrada(delta, epsilon)
        termo1= (-1*b)/(2*a)
        x1= raiz/(2*a)
        x2= raiz/(2*a)
        print('reais complexas')
        print('%.4f %.4fi' %(termo1,x1))
        print('%.4fi %.4fi' %(termo1,x2))
        
        
else:
    print('ERRO: equação não é do segundo grau')