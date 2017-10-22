 -*- coding: utf-8 -*- 
vi=int(input("Volume Inicial: "))
nt=int(input("Número de trocas: "))
vol=vi
for i in range (0,nt,1):
    vt=int(input("Troca de volume: "))
    vol=vol+vt
    if vol >= 100:
        vol=100
    if vol <= 0:
        vol=0
print (vol)