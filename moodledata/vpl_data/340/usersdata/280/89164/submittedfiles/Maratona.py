# -*- coding: utf-8 -*-
np=int(input("Número de postos: "))
dim=int(input("Distância intermediária máxima: "))
local=42195/np
ploc=0
cont=0
for i in range (0,np,1):
    p=int(input("Localização do posto: "))
    ploc=p-ploc
    if p > local:
        cont=cont + 1
if cont == 0:
    print ("S")
if cont != 0:
    print ("N")
    