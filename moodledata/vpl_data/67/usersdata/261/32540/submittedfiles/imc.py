# -*- coding: utf-8 -*-
def imc(peso,altura):
    ind = peso/(altura**2)
    if (ind<20):
        print ("Seu IMC está ABAIXO do normal")
    elif (ind >= 20) and (ind<=25):
        print ("Seu IMC está NORMAL")
    elif (ind > 25) and (ind<=30):
        print ("Seu IMC está com SOBREPESO")
    elif (ind > 30) and (ind<=40):
        print ("Seu IMC está com OBESIDADE")
    ELif (ind<40):
        print ("Seu IMC está com OBESIDADE GRAVE")
print ("================================")
peso = input("Digite o seu peso em quilogramas! ")
altura = input("Digite a sua altura em metros! ")
print ("================================")

imc(peso,altura)

        
        

