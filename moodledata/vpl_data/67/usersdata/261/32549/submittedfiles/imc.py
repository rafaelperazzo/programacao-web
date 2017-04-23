# -*- coding: utf-8 -*-
def imc(peso,altura):
    ind = peso/(altura*altura)
    if (ind<20):
        print ("Seu IMC está marcando ABAIXO do normal")
    elif (ind >= 20) and (ind<=25):
        print ("Seu IMC está marcando NORMAL")
    elif (ind > 25) and (ind<=30):
        print ("Seu IMC está marcando SOBREPESO")
    elif (ind > 30) and (ind<=40):
        print ("Seu IMC está marcando OBESIDADE")
    elif (ind>40):
        print ("Seu IMC está marcando OBESIDADE GRAVE")
        
print ("====================================")
pe = float(input("Digite o seu peso em quilogramas! "))
al = float(input("Digite a sua altura em metros! "))
print ("====================================")

imc(pe,al)

        
        

