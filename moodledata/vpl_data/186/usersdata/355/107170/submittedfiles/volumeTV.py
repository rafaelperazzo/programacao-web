# -*- coding: utf-8 -*- 
 
volumei= int(input('Digite o volume inicial da televisão: '))
trocas = int(input('Digite o número de trocas de volume feitas: '))
volumef=0
for i in range(0,trocas,1):
    numt=int(input('Digite a troca feita: '))
    volumef=volumei+volumef+numt
    if volumef>100:
        volumef=100
    elif volumef<0:
        volumef=0
print(volumef)