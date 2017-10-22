from minha_bib import *














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





