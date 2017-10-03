# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n = int(input("Digite um número: "))
if n>500 and n<1000:
    print("Este número está compreendido entre 500 e 1000")
    if n==5:
        print("Este número é igual a 5")
    if n==200:
        print("Este número é igual a 200")
    if n==500:
        print("Este número é igual a 500")
else:
    print("Este número não pertence a nenhum dos escopos")