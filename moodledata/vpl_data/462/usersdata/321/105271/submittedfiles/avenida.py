# -*- coding: utf-8 -*-
M= int(input('Número de quadras no sentido Norte-Sul: '))
while 2<m and m<1000:
    m=int(input('Número de quadras no sentido Norte-Sul: '))
    
N= int(input('Número de quadras no sentido Leste-Oeste: '))
while 2<n and n<1000:
    n= int(input('Número de quadras no sentido Leste-Oeste: '))
    
quadras= []

for i in range(0,n, 1):
    linha= []
    linha.append(
