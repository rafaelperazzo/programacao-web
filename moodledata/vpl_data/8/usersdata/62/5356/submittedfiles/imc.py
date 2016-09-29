# -*- coding: utf-8 -*-
from __future__ import division
#ENTRADA
peso=input("Digite seu peso: ")
altura=input("Digite sua altura: ")

#PROCESSAMENTO

imc=peso/(altura**2)

#SAIDA

if imc<20:
    print("ABAIXO")
else:
    if 20<=imc<=25:
        print("NORMAL")
    else:
        if 25<=imc<=30:
            print("SOBREPESO")
        else:
            if 30<=imc<=40:
                print("OBESIDADE")
            else:
                print("OBESIDADE GRAVE")
    
