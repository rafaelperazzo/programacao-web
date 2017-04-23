# -*- coding: utf-8 -*-
import math
cv=int(input("Digite o numero de vitorias do Cormengo:" ))
ce=int(input("Digite o numero de empates do Cormengo: "))
cg=int(input("Digite o numero de gols do Cormengo: "))
fv=int(input("Digite o numero de vitorias o Flaminthians: "))
fe=int(input("Digite o numero de empates do Flaminthians: "))
fg=int(input("Digite o numero de gols do Flaminthias:  "))
if cv>fv:
    print("C")
elif cv<fv:
    print("F")
elif cv==cf:
    if ce>fe:
        print("C")
    elif ce<fe:
        print("F")
    elif ce==fe:
        if cg>fg:
            print("C")
        elif cg<fg:
            print("F")
        elif cg==fg:
            print("=")