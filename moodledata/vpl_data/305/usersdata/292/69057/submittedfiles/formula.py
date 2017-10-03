# -*- coding: utf-8 -*-
print("--------------------------------------------------------")
print("Seja muito bem vindo!!")
print("--------------------------------------------------------")
cont=0
while cont!=1:
    P=float(input("\nDigite o valor de P: "))
    i=float(input("Digite o valor de i: "))
    n=float(input("Agora digite o valor de n: "))
    v=P*((((1+i)**n)-1)/i)
    print("\nv é igual a %.2f"%v)
    cont=int(input("\n\nDeseja continuar? (Digite 1 para encerrar e outro número para continuar): ")