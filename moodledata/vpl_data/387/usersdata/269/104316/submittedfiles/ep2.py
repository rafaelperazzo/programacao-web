# -*- coding: utf-8 -*-
''' Equipe: David Willian Gonçalves Silveira e Maria Luana Bezerra de Lima '''
''' Número de matrúcilas: 405389 e 405958 '''
''' Exercicio-Programa 2 -- Razão Aurea '''
'''ECI0007 (EC) -- 2017 -- Professor: Rafael Perazzo '''
''' Interpretador: Python versão 3 '''

#COMECE SEU CODIGO NA LINHA ABAIXO.
m=0
while m<1 or m>2000:
    m=float(input('digite m: '))
e=0    
while e<=0 or e>=1:
    e=float(input('digite e: '))
    
if (m//2)==0:
    a=2
    b=3
    c=4
    cont=0
    for i in range(0,(m/2),1):
        cont=cont+ (4/(a*b*c))
        a=a+4
        b=b+4
        c=c+4
print(cont)  