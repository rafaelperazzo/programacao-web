# -*- coding: utf-8 -*- 
 
volumei= int(input('Digite o volume inicial da televisão: '))
trocas = int(input('Digite o número de trocas de volume feitas: '))
volumef=0
maxi=100-volumei
mini=volumei
for i in range(0,trocas,1):
    numt=int(input('Digite a troca feita: '))
    volumei=volumei+numt
    if volumei>100:
        volumei=100
    elif volumei<0:
        volumei=0
print(volumei)