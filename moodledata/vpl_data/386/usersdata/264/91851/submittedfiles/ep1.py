# -*- coding: utf-8 -*-
'''
Equipe: Aurélio Bento do Nascimento, Aparecido Petrison Belém Batista.
Número de matrícula: 405386, 405944
Exercício-Programa 1 -- Raízes de Equações Quadráticas
ECI0007 -- 2017 -- Professor: Rafael Perazzo
Interpretador: Python versão 3
'''
def raiz_quadrada(x,y):
    r=x
    while True:
        rq=(1/2)*(r+(x/r))
        if (abs(r-rq)<y):
            return(rq)
        r=rq
n = int(input('digite a quantidade de equações: '))
y = float(input('digite a precisão das raízes: '))
cont=0
while (cont<n):
    a = float(input('digite  valor de a: '))
    b = float(input('digite  valor de b: '))
    c = float(input('digite  valor de c: '))
    if (a==0):
        print(a)
        print(b)
        print(c)
        print('ERRO: a equação não é do segundo grau!')
    if (a!=0):
        delta=(b**2)-(4*a*c)
        if (delta>0):
            raiz=raiz_quadrada(delta,y)
            X1=(-b-raiz)/(2*a)
            X2=(-b+raiz)/(2*a)
            if (X1!=X2):
                print(a)
                print(b)
                print(c)
                print('As raízes são do tipo reais simples')
                print('%.5f' %X1)
                print('%.5f' %X2)
        if (delta==0):
            raiz=0
            X1=(-b-raiz)/(2*a)
            X2=(-b-raiz)/(2*a)
            if (X1==X2):
                print(a)
                print(b)
                print(c)
                print('As raízes são do tipo reais duplas')
                print('%.5f' %X1)
                print('%.5f' %X2)
        if (delta<0):
            delta=delta
            complexo=raiz_quadrada(delta,y)
            X1=(-b)/(2*a)
            X2=(-b)/(2*a)
            complexo_1=-complexo/(2*a)
            complexo_2=complexo/(2*a)
            print(a)
            print(b)
            print(c)
            print('As raízes são do tipo complexas')
            print(complexo_1)
            print(complexo_2)
    break