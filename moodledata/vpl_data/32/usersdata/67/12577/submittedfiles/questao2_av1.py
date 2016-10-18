# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO
nmr1y=input("Digite o primeiro numero de sua escolha:")
nmr2y=input("Digite o segundo numero de sua escolha:")
nmr3y=input("Digite o terceiro numero de sua escolha:")
nmr4y=input("Digite o quarto numero de sua escolha:")
nmr5y=input("Digite o quinto numero de sua escolha:")
nmr6y=input("Digite o sexto numero de sua escolha:")

nmr1s=input("Digite o primeiro numero sorteado:")
nmr2s=input("Digite o segundo numero sorteado:")
nmr3s=input("Digite o terceiro numero sorteado:")
nmr4s=input("Digite o quarto numero sorteado:")
nmr5s=input("Digite o quinto numero sorteado:")
nmr6s=input("Digite o sexto numero sorteado:")

cont=0

if nmr1y==nmr1s or nmr1y==nmr2s or nmr1y==nmr3s or nmr1y==nmr4s or nmr1y==nmr5s or nmr1y==nmr6s:
    cont=cont+1
    
if nmr2y==nmr1s or nmr2y==nmr2s or nmr2y==nmr3s or nmr2y==nmr4s or nmr2y==nmr5s or nmr2y==nmr6s:
    cont=cont+1

if nmr3y==nmr1s or nmr3y==nmr2s or nmr3y==nmr3s or nmr3y==nmr4s or nmr3y==nmr5s or nmr3y==nmr6s:
    cont=cont+1    

if nmr4y==nmr1s or nmr4y==nmr2s or nmr4y==nmr3s or nmr4y==nmr4s or nmr4y==nmr5s or nmr4y==nmr6s:
    cont=cont+1

if nmr5y==nmr1s or nmr5y==nmr2s or nmr5y==nmr3s or nmr5y==nmr4s or nmr5y==nmr5s or nmr5y==nmr6s:
    cont=cont+1
    
if nmr1y==nmr6s or nmr6y==nmr2s or nmr6y==nmr3s or nmr6y==nmr4s or nmr6y==nmr5s or nmr6y==nmr6s:
    cont=cont+1 
    
if cont==3:
    print("terno")
if cont==4:
    print("tuadra")
if cont==5:
    print("quina")
if cont==6:
    print("sena")
if cont<3:
    print("azar")