# -*- coding: utf-8 -*-
peso=float(input("Digite seu peso em kilos: "))
altura=float(input("Digite sua altura em metros: "))
IMC=(peso/(altura**2))
if IMC<20:
    print("ABAIXO")
elif 20<=IMC<=25:
    print ("NORMAL")
else 25<IMC<=30:
    print ("SOBREPESO")
else 30<IMC<=40:
    print ("OBESIDADE")
elif IMC>40:
    print ("
    
    

