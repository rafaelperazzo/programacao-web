# -*- coding: utf-8 -*-

n = int(input('informe quantidade de termos: '))
while n < 2:
    n = int(input('informe quantidade de termos: '))

l1 = []

for i in range (0,n,1):
    l1.append(int(input('informe o %d° elemento da lista: ' %(i+1))))

