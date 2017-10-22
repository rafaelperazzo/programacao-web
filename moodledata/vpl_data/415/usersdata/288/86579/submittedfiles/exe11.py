# -*- coding: utf-8 -*-
n=int(input("Digite um numero de oito digitos "))
if n<10000000 or n>99999999:
    print ("NAO SEI")
else:
    s=0
    while (n>0):
        resto=n%10
        n=(n-resto)/10
        s+=resto
    print ("%.f" %s)
else:
    print ("NAO SEI")