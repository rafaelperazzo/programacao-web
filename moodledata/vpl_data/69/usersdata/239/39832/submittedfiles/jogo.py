# -*- coding: utf-8 -*-
import math
Cv=int(input("Digite o número de vitorias do Cormengo: "))
Ce=int(input("Digite o número de empates do Cormengo: "))
Cs=int(input("Digite o saldo de gols do Cormengo: "))
Fv=int(input("Digite o número de vitorias do Flamintias: "))
Fe=int(input("Digite o número de empates do Flamintias: "))
Fs=int(input("Digite o saldo de gols do Flamintias: "))

if Cv>Fv:
    print("F")
elif Fv>Cv:
    print("C")
else:
    if Ce>Fe:
        print("C")
    elif Fe>Ce:
        print("F")
    else:
        if Cs>Fs:
            print("C")
        elif Fs>Cs:
            print("F")
        else:
            print(=)