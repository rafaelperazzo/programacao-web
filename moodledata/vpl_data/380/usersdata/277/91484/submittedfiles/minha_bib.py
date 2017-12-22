# -*- coding: utf-8 -*-
def mostrar_na_tela(texto) :
    print(texto)
    return

def fatorial(n) :
    f = 1
    for i in range(2,n+1,1) :
        f *= i
    return f

def ler_inteiro() :
    while(True):
        n = int(input("Digite um numero inteiro positivo: "))
        if (n >= 0) :
            break
    return n