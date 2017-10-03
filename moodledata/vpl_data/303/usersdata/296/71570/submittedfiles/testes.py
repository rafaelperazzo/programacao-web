# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
a = input("Que horas  são? [0-23]: ")
#Processamento e saída
if a>3 and a<12:
    print("Bom dia")
elif a >= 12 and a < 18:
    print("Boa tarde")
else:
    print("Boa noite")
