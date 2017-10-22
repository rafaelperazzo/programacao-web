from minha_bib import *

nota1 = ler_inteiro()
nota2 = ler_inteiro()
print (media(nota1,nota2))















"""
while(True):
    while(True):
        n = int(input("Digite um numero inteiro positivo: "))
        if (n >= 0) :
            break
    f = 1
    for i in range(2,n+1,1) :
        f *= i
    print("%d! = %d" % (n,f))
    opt = input("Deseja continuar? [S ou N] ")
    if (opt == 'N') :
        print("\n\nATE BREVE!")
        break
"""






















"""

# DEFINI A FUNCAO
def fatorial(n) :
    f = 1
    for i in range(2,n+1,1) :
        f *= i
    return f
    
# VOU USAR
while(True):
    while(True):
        n = int(input("Digite um numero inteiro positivo: "))
        if (n >= 0) :
            break
    fat = fatorial(n)
    print("%d! = %d" % (n,f))
    opt = input("Deseja continuar? [S ou N] ")
    if (opt == 'N') :
        print("\n\nATE BREVE!")
        break

"""





