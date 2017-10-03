# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n = int(input("DIGITE UM NÚMERO: "))
if n%10==0:
    print("È divisível por 10")
elif n%5==0:
    print("È divisível por 5")
elif n%2==0:
    print("È divisível por 2")
else:
    print("Não é divisível por 10, 5 e 2")