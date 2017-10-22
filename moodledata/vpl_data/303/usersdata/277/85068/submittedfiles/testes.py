#from minha_bib import *

def media(n1,n2) :
    m = (n1+n2)/2.0
    return m

x = float(input('Digite nota 1: '))
y = float(input('Digite nota 2: '))

m = media(x,y)
z = m * 0.25

print( z )

print(multiplicacao(2,3))












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





