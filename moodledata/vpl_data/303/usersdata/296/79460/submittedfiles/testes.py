# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n = int(input("Digite um número: "))
if n==5:
    print("Este número é igual a 5")
    if n>500 and n<1000:
        print("Este número está compreendido entre 500 e 1000")
    else:
        print("Este número não está compreendido entre 500 e 1000")
elif n==200:
    print("Este número é igual a 200")
    if n>500 and n<1000:
        print("Este número está compreendido entre 500 e 1000")
    else:
        print("Este número não está compreendido entre 500 e 1000")
elif n==500:
    print("Este número é igual a 500")
    if n>500 and n<1000:
        print("Este número está compreendido entre 500 e 1000")
    else:
        print("Este número não está compreendido entre 500 e 1000")
elif n>500 and n<1000:
    print("Este número está compreendido entre 500 e 1000")
    else:
    print("Este número está fora dos escopos")