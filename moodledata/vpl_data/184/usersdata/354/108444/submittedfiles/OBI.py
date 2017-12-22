# -*- coding: utf-8 -*-

n=int(input('Digite o numero de participantes: '))
p=int(input('Digite a pontuação mínima necessária: '))
cont=0
for i in range (0,n,1):
    pont1=int(input('digite a pontuação da 1º fase: '))
    pont2=int(input('digite a pontuação da 2º fase: '))
    if pont1+pont2>=p:
        cont=cont+1

print(cont)