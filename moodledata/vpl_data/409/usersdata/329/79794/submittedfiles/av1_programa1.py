# -*- coding: utf-8 -*-
numero = int(input("digite o valor de numero="))
PAR = (numero*0.5)
z = PAR%2
q = PAR%4
s = PAR%6
o = PAR%8
if z or q or s or o :
    print("PAR")
else :
    print("IMPAR")


