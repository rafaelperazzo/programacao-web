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
E = float(input('digte o valor de E: '))
print(a)
print(b)
print(c)
if a==0:
    print('ERRO: equação não é do segundo grau')
else: 
    delta=(b**2)-(4*a*c)
    if delta>0:
        print('real dupla')
        while abs(proximo-ro1)>=E:
            r01=(delta+1)/2
            r02=r01
            proximo=(r02+1)/2
            proximo=(proximo+1)/2
            print(proximo)
    if delta==0:
        print('reais simples')
    if delta<0:
        print('complexas')




    