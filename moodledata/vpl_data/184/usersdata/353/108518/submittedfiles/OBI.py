# -*- coding: utf-8 -*-
n=int(input(número de participantes:'))
p=int(input('poontuação mínima necessária:'))
cont=0
for i in range (0,n,1):
    pont1=int(input('pontuação 1:'))
    pont2=int(input('pontuação 2:'))
    if pont1+pont2>=p :
        cont=cont+1
print (cont)