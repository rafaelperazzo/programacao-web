# -*- coding: utf-8 -*-

volumei=int(input('digite o volume inicial da televisao: '))
trocas= int(input('digite o numero de trocas de volumes feitas: '))

for i in range(0,trocas,1):
    numt=int(input('digite a troca feita: '))
    volumei=volumei+numt
    if volumei>100:
        volumei=100
    elif volumei<0:
        volumei=0

print(volumei)
