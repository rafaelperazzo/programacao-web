# -*- coding: utf-8 -*-
'''
Equipe: Aurélio Bento do Nascimento, Aparecido Petrison Belém Batista.
Número de matrícula: 405386, 405944
Exercício-Programa 1 -- Raízes de Equações Quadráticas
ECI0007 -- 2017 -- Professor: Rafael Perazzo
Interpretador: Python versão 3
'''
a = float(input('digte o valor de a: '))
b = float(input('digte o valor de b: '))
c = float(input('digte o valor de c: '))
print(a)
print(b)
print(c)
delta=(b**2)-(4*a*c)
if delta>0:
    print('real dupla')
if delta==0:
    print('reais simples')
if delta<0:
    print('complexas')

    