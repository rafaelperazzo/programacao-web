# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO

n = input("Digite o número: ")
i=0
while i*(i+1)*(i+2)==n:
    i=i+1
if i*(i+1)*(i+2)<=n:
    print ("Sim")
else:
    print("Não")
        