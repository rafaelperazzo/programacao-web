# -*- coding: utf-8 -*-
import math

x1 = int(input("Digite o seu primeiro número: "))
x2 = int(input("Digite o seu segundo número: "))
x3 = int(input("Digite o seu terceiro número: "))
x4 = int(input("Digite o seu quarto número: "))

if (x1>x2 and x2>=x3 and x3>=x4) :
    print("'S'")
else:
    if (x1<x2 and x2 > x3 and x3>=x4):
        print("'S'")
    else:
        if (x1<=x2 and x2<x3 and x3>x4):
            print("'S'")
        else:
            if (x1<= x2 and x2<=x3 and x3<x4):
                print("'S'")
            else:
                print("'N'")
    