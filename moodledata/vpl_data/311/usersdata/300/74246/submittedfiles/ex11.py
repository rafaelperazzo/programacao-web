# -*- coding: utf-8 -*-
d = int(input('Digite o dia da data 1: '))
m = int(input('Digite o mês da data 1: '))
a = int(input('Digite o ano da data 1: '))
D = int(input('Digite o dia da data 2: '))
M = int(input('Digite o mês da data 2: '))
A = int(input('Digite o ano da data 2: '))
if a > A:
    print('DATA 1')
if a == A and m > M:
    print('DATA 1')
if a == A and m == M and d > D:
    print('DATA 1')
if a < A:
    print('DATA 2')
if a == A and m < M:
    print('DATA 2')
if a == A and m == M and d < D:
    print('DATA 2') 
if a == A and m == M and d == D:
    print('IGUAIS')