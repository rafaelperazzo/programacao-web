# -*- coding: utf-8 -*-
n=int(input('Digite o numero de participantes: '))
p=int(input('Digite a pontuaao minima necessaria: '))
cont=0
for i in range(0,n,1):
    pont1=int(input('Digite a pontuaao da primeira fase: '))
    pont2=int(input('Digite a pontuaçao da segunda fase: '))
    if pont1+pont2>=p:
        cont=cont+1
        
print(cont)